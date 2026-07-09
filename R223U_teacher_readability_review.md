# R223U teacher readability review

## Question

Does the sandbox preview keep teacher default draft readable?

## Judgment

```text
TEACHER_DEFAULT_DRAFT_READABILITY = PASS_WITH_PREVIEW_NOTES
```

## Evidence

The center panel is the teacher draft preview. It is visually stronger than the review ledger and contains natural manuscript paragraphs rather than backend field lists.

The draft does not show:

- `practice_pattern_type`
- `demonstration_type`
- `micro_practice_type`
- `appreciation_scaffold_type`
- `component_trigger`
- `screen_trigger`
- `learning_sheet_fields`
- `evidence_outputs`

## Notes

R223T intentionally uses shortened teacher draft excerpts, not full final manuscripts. This is acceptable for sandbox review. If R223V or later requires teacher review of full drafts, the center panel should support full manuscript reading and may need a document-style view.

## Hold triggers

Hold if future preview:

- lets ledger text dominate the teacher draft
- exposes backend fields in the teacher draft
- turns teacher draft into a card wall
- offers apply/save controls

