# Homework 2 — Welfare and risk

Preparation draft for Lectures 3 and 4, in English and the established NES
course style. **Deadline: to be announced.**

- [Complete student assignment](homework02.pdf?raw=true)
- [Instructor solutions and marking scheme](instructor-solutions.pdf?raw=true)
- [All PDFs and editable LaTeX](homework02-complete.zip?raw=true)

## Order and assessment

The **9-page student PDF** puts training first and the timed mock second.

- **Part I, pages 1–3:** the ordinary assessed homework, 100 points. Three
  compulsory problems are worth 30, 35 and 35. The three assessed homework
  scores remain equally weighted within the course's 20% homework component.
- **Part II, pages 4–9:** a 120-minute formative mock, 100 diagnostic points.
  Ten true/false claims are worth 5 each; two problems are worth 20 each;
  two short answers are worth 5 each and limited to three sentences each.
  Mistakes in this part do not lower the course grade.

The two scores are separate. Solutions are handwritten. Students work through
the assessed training with resources first, then put it aside for the mock's
recommended closed-resource diagnostic. This is not a final-exam materials policy.
AI assistance in the ordinary homework must be disclosed and the student must
be able to explain their work, as in Homework 1.

One SOSD coupling exercise follows Training 2 in the **same PDF**. It is
ungraded, not submitted and not part of either point total. There is no separate
optional-practice handout.

## Material and planned Lecture 4 scope

Lecture 3's duality, Roy, Shephard and Slutsky are combined with a planned
Lecture 4 opening on **CV, EV and consumer-surplus changes**, followed by
expected utility, certainty equivalents, risk premiums, Arrow–Pratt measures
and insurance. FOSD is included; SOSD is additional practice only. Lecture 4
slides have not yet been prepared in this repository, so this is a preparation
draft for that proposed combined welfare/risk lecture.

The assessed training covers:

1. Start from expenditure, recover demand and indirect utility, then compare
   CV, EV, finite CS loss and the cost of keeping an old basket affordable.
2. Compare two lotteries, CEs, risk premiums, risk attitudes and FOSD;
   optional conditional Jensen shows SOSD.
3. Solve fair and loaded log-utility insurance, then vary initial wealth.

The mock uses a different consumer function (harmonic utility) and square-root
insurance, plus ten theory claims and two short economic explanations. All
welfare numbers use an explicit **positive-loss** sign convention. CS is a
finite change, not an absolute surplus integral to an infinite choke price.

## Instructor files

`instructor-solutions.pdf` gives complete analytical solutions, all answers and
subpart marking. The true/false key is **T, F, F, F, T; T, F, T, F, F**.
The ZIP includes answers; send students only `homework02.pdf`.

## Build and checks

Run `bash build.sh` with XeLaTeX, DejaVu Sans and the standard article packages.
For Overleaf, upload the whole folder including `assets/`, select XeLaTeX and
choose `homework02.tex` or `instructor-solutions.tex` as the main file.

`python3 verify-examples.py` uses only the Python standard library. It checks
**75 parameter/data cases** with independent feasible grids, finite-difference
envelopes, numerical CS integrals, welfare bounds, lotteries and insurance,
plus a grading-total audit.

The complete ZIP contains all PDFs, editable sources, style, original NES logo,
build script, verification script and documentation under `homework02/`.
See [REVIEW.md](REVIEW.md) for the coverage and mathematical audit.
