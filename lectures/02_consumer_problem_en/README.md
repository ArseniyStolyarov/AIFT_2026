# Microeconomics 2 — The Consumer Problem

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.

## Downloads

- [Presentation with reveals](lecture02.pdf?raw=true)
- [Handout: one final state per slide](handout.pdf?raw=true)
- [Instructor notes](instructor-notes.pdf?raw=true)
- [All PDFs and editable LaTeX](lecture02-complete.zip?raw=true)
- [Slide index](slide-index.md)

The condensed deck has **59 main slides and 5 reserve slides**: 64 logical
slides, 261 presentation pages with click-by-click reveals. The first eleven
slides are unchanged, including their appearance.

## Live sequence

- **1–11:** budgets, existence, Marshallian demand and homogeneity.
- **12–13:** one Lagrangian-intuition slide and one saddle-definition slide.
- **14–17:** saddle implies consumer optimum, with a four-part proof plan.
- **18–26:** an optimum yields a saddle under concavity and differentiability;
  multiplier construction, signs, stationarity, slackness, both saddle inequalities
  and the zero-bundle case are all proved.
- **27:** the four KKT conditions as a single recap.
- **28–37:** Cobb–Douglas, then Walras' law, substitutes and a numerical corner,
  linear-plus-log utility with income/price corners, and complements.
- **38–39:** convex preferences give convex demand; strict convexity gives uniqueness.
- **40–46:** define indirect utility, compute values for all four models and
  discuss its properties and possible kinks.
- **47–52:** the general constrained smooth-branch envelope theorem and proof;
  derivatives in income and prices.
- **53–58:** Roy's identity, its direct proof and model applications.
- **59:** reading and next steps.
- **60–64:** a small expenditure-minimisation reserve for the next lecture.

There is no long leftover proof appendix and no student-facing staging label.
English text, the supplied NES logo, course colours, generous spacing and
question-before-answer reveals are retained.

## Mathematical qualifications

For the saddle theorems use the full Lagrangian
`L=u+lambda*(m-p*x)+mu*x`, with nonnegative multipliers. Its quantity domain is
an open convex set U where u is defined; feasibility additionally requires
nonnegative quantities and the budget. The forward theorem needs no smoothness
or concavity; the converse assumes differentiability and concavity on U.
Log Cobb–Douglas is used only after the original product index rules out axes.

The general envelope version assumes C1 data and a C1 selection of optimal
quantities and KKT multipliers near an interior parameter. All chain-rule terms
are shown before they vanish. Roy has a separate fixed-bundle proof and does
not require a smooth direct utility or differentiable demand. The quasilinear
example is `a+4*log(1+q)` with budget `a+r*q<=m`; at unit prices its target is q=3.

Homework 1 covers Lectures 1–2 and is due on 14 November 2026. Source-course
homework announcements were not imported. Inputs were the supplied Lectures 10
and 11; source qualifications are in `SOURCE_NOTES.md`.

## Build

Run `bash build.sh` with XeLaTeX, Beamer, TikZ/pgfplots, fontspec, polyglossia and
DejaVu Sans installed. No network or credentials are needed. Three PDFs are
compiled twice; temporary output stays in `build/`. The complete ZIP contains a
self-contained source ZIP, PDFs, notes and index. Optional independent numerical
checks: `python3 verify-examples.py` (standard library only).
