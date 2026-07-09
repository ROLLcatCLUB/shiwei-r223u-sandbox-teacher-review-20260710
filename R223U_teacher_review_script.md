# R223U teacher review script

stage_id: 1013R_R223U_SANDBOX_TEACHER_REVIEW  
status: sandbox_teacher_review_only  
source: R223T_FIXTURE_ONLY_SANDBOX_PREVIEW

## Review target

Review the R223T standalone sandbox preview as a teacher/reviewer.

This review is not a product launch review and not a formal UI review.

## Teacher walkthrough tasks

### 1. Identify the page status

Ask:

```text
Can I immediately tell this is a preview-only sandbox, not a published product route?
```

Expected visible signals:

- `fixture_only=true`
- `non_persistent_preview=true`
- `teacher_confirmed=false`
- `formal_apply_allowed=false`
- `Preview only. v0.2 candidate is not published. No lesson body writeback.`

### 2. Understand v0.1 / v0.2 comparison

Ask:

```text
Can I understand what v0.2 improves without reading backend schema files?
```

Expected:

- v0.1 baseline is short.
- v0.2 candidate delta is short.
- The difference is about classroom expansion density and unit role, not just "more fields".

### 3. Read teacher default draft

Ask:

```text
Is the center draft still the main reading object?
```

Expected:

- The teacher draft is in the center.
- It reads as a teacher manuscript.
- It does not show backend field names.

### 4. Inspect review ledger

Ask:

```text
Is the ledger useful for review but clearly secondary?
```

Expected:

- It is labeled review-only.
- It shows event count, primary patterns, component trigger status and mapping.
- It does not look like the teacher's final manuscript.

### 5. Check component semantics

Ask:

```text
Do component trigger statuses look like metadata rather than executable classroom tools?
```

Expected:

- No run/open/insert/apply controls.
- Component status is text only.
- New surface candidates do not look available for use.

### 6. Compare the three samples

Ask:

```text
Can I see why the three samples have different classroom expansion density?
```

Expected:

- M_stationery: high practice creation.
- N_paper_print: medium technique preparation.
- O_color_collision: medium intro understanding.

## Review outcome options

```text
PASS_CONTINUE_TO_R223V_SANDBOX_REDUCTION_OR_PILOT_HOLD
HOLD_FOR_R223T_SANDBOX_PREVIEW_REDUCTION
HOLD_FORMAL_V0_2_NOT_READY
```

