# Supplier workflow: approved demo requirements

These are fictional customer business rules inspired by the accompanying legal
brief. They are not universal LkSG/CSDDD statutory requirements. The brief's
reporting suspension does not authorise this system to delete documentation.

## SUP-01 — Assessment before approval
A supplier can be approved only when assessment_status is completed. Pending
and missing assessments must block approval even when all numeric risks are 0.

## SUP-02 — Severe risk overrides averages
Risk dimensions are integers 0–100. Any individual dimension >= 80 blocks
approval and requires manual review. An average below 80 must never override
an individual severe risk. Unknown/missing risk dimensions also block approval.

## RET-01 — Documentation retention
This demo retains documentation for at least seven calendar years from creation.
For a 29 February creation date, use 1 March in the seventh year if that year has
no 29 February. Records remain retained until that anniversary. An active legal
hold blocks deletion regardless of age. The API returns eligibility only; it
never deletes records.

## Review evidence
When identifying a defect, cite the applicable rule ID and document, provide a
concrete input and the incorrect output, and suggest a correction. Distinguish
these customer rules from legal requirements. Do not certify legal compliance.
