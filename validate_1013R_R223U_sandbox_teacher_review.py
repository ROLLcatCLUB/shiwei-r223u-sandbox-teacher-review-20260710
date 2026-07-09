import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223U_teacher_review_script.md",
    "R223U_sandbox_review_checklist.md",
    "R223U_teacher_readability_review.md",
    "R223U_v0_1_vs_v0_2_understandability_review.md",
    "R223U_review_ledger_weight_review.md",
    "R223U_component_trigger_semantics_review.md",
    "R223U_continue_or_hold_decision.md",
    "R223U_decision_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

REQUIRED_DECISIONS = [
    "PASS_CONTINUE_TO_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD",
    "HOLD_FOR_R223T_SANDBOX_PREVIEW_REDUCTION",
    "HOLD_FORMAL_V0_2_NOT_READY",
]

REQUIRED_PHRASES = [
    "preview-only",
    "v0.2 not published",
    "teacher default draft",
    "review ledger",
    "component trigger",
    "metadata",
    "not executable",
    "v0.1 / v0.2",
    "practice_intensity",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "FORMAL_UI = BLOCKED",
    "R97B_ROUTE = BLOCKED",
    "RUNTIME_PROVIDER_MODEL_PROMPT_DB = BLOCKED",
    "LESSON_BODY_WRITEBACK = BLOCKED",
]

FALSE_BOUNDARIES = [
    "schema_v0_2_published",
    "formal_ui",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_apply",
]

BANNED_PHRASES = [
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "FORMAL_UI = ALLOWED",
    "R97B_ROUTE = ALLOWED",
    "teacher_confirmed=true",
    "formal_apply_allowed=true",
    "database_written=true",
    "lesson_body_written=true",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists())

    for decision in REQUIRED_DECISIONS:
        checks += 1
        if decision not in combined:
            failures.append(f"missing decision output: {decision}")

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in BANNED_PHRASES:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden phrase present: {phrase}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223U_SANDBOX_TEACHER_REVIEW":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD":
            failures.append("manifest decision mismatch")
        boundaries = manifest.get("boundaries", {})
        for key in FALSE_BOUNDARIES:
            checks += 1
            if boundaries.get(key) is not False:
                failures.append(f"manifest boundary must be false: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD",
    }
    (ROOT / "validate_1013R_R223U_sandbox_teacher_review_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

