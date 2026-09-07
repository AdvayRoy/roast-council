# Case name

Completed work with prioritized repairs

## Input

ROAST the completed repository for a small appointment-booking tool. The core booking flow works, the target user can create an appointment in under two minutes, the README explains setup, and the happy path has automated tests. Review found that an expired invite link returns a blank page instead of a recoverable error, the admin export omits the timezone, and the button spacing is inconsistent on one screen. No data loss or unauthorized access has been observed. The next customer demo is in three days.

## Expected profile

Completed Work Review with Technical Architecture and Product / Feature secondary lenses.

## Expected core behavior

The response must include `WHAT WORKS`, `FAILURES`, `P0`, `P1`, `P2`, `EXACT REPAIRS`, and `VERDICT`. It should preserve the working booking flow and README. The blank expired-link state and timezone omission should be prioritized by user impact and correctness; spacing is P2 unless evidence shows it blocks use. Judge should choose `FIX THEN SHIP` if the blank state or export is material, not `REWORK`, and should name the smallest patches before the demo.

## Fail conditions

- Recommends rewriting the repository because two edge cases exist.
- Calls every issue P0 or treats spacing as a release blocker without evidence.
- Ignores what already works.
- Gives no exact repair or ship boundary.

## Good verdict range

`FIX THEN SHIP`, with the expired-link and timezone repairs prioritized and spacing deferred; `SHIP` is acceptable only with a justified scope decision and a clear follow-up.

## Notes

This case checks severity discipline, exact repairs, and the ability to ship good completed work after small fixes.
