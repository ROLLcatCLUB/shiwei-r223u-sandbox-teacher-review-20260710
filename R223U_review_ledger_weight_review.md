# R223U review ledger weight review

## Question

Does the review ledger support audit without overtaking the teacher draft?

## Judgment

```text
REVIEW_LEDGER_WEIGHT = PASS_WITH_COLLAPSE_NOTE
```

## Current behavior

The ledger is on the right, labeled:

```text
Review-only metadata. Not executable. Not written back.
```

It shows:

- event count
- primary patterns
- component trigger status
- screen / sheet / evidence mapping

## Why it passes

The ledger is clearly secondary and does not pretend to be teacher default draft.

## Why it still needs caution

At narrower widths or in any future pilot, the ledger could become visually heavy. Recommended later behavior:

- teacher draft open by default
- ledger collapsed by default or summary-first
- full ledger available only after explicit review action

## Hold condition

Hold if future preview makes the ledger the main reading surface.

