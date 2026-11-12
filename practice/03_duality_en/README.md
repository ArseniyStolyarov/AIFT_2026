# Seminar 3 — Demand and duality

An English problem sheet for the teaching assistant, in the NES course style,
with a separate full instructor key. No instructor name appears in the footer
or PDF author metadata.

- [Student worksheet](seminar03.pdf?raw=true)
- [Instructor solutions](instructor-solutions.pdf?raw=true)
- [Entire folder: PDFs and LaTeX](seminar03-complete.zip?raw=true)

## Contents

Six short true/false statements precede two multi-part problems:

1. **A little of everything:** `sqrt(x1) + 2 sqrt(x2)`. Strict concavity,
   positivity, direct Marshallian/Hicksian optimisation, both value functions,
   Roy, Shephard, duality and a numerical own-price Slutsky decomposition.
   The full Slutsky matrix is compulsory: construct it from Marshallian demand,
   check symmetry, multiply by the price vector, check negative semidefiniteness,
   then prove the general result using expenditure.
2. **Two escape routes and a head start:** `max{x1 + 1, sqrt(x2)}`.
   Continuous LNS preferences with a nonconvex upper contour set; the chosen
   corner switches twice with income at prices `(9/2,1)`.
   Derive complete demand correspondences, recover quantities from values in
   each strict regime, match the duality boundaries and examine the exact tie.
   Two optimisers at a tie do not imply an optimal midpoint. Targets above the
   baseline utility 1 are distinguished from targets already met at zero.

The student sheet has **3 pages**, the full key **8 pages**.
The key suggests a 90-minute route. Matrix calculation and the general theorem
are core material. The optional last question is a tangential tie at `(4,1)`:
an income derivative exists, but the full price gradient does not.
It contains all answers, the branch conditions and an upper-contour diagram.
Only `seminar03.pdf` is the student handout; the ZIP includes the answer key.

## Build and verify

Run `bash build.sh` with XeLaTeX, DejaVu Sans, the standard article packages
and TikZ installed. Both PDFs are built twice. For Overleaf, upload the whole
folder including `assets/`, select XeLaTeX, and choose `seminar03.tex` or
`instructor-solutions.tex` as the main file.

Run `python3 verify-examples.py` for independent feasible-grid, finite-difference
and boundary-set checks. It uses only Python's standard library and checks
**208 parameter/data cases**, including both crossings, the tangency and
targets below the baseline.

The complete ZIP contains the student PDF, key PDF, all editable sources,
style, logo, build script, verification script and this documentation under
`seminar03/`.

See [REVIEW.md](REVIEW.md) for coverage and the audit against previous material.
