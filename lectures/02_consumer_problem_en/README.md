# Microeconomics 2 — The Consumer Problem

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.

Prepared from the supplied **Lecture 10** and **Lecture 11** handouts.

## Documents

- `lecture02.pdf`: presentation with click-by-click reveals.
- `handout.pdf`: all final reveal states, one page per logical slide.
- `instructor-notes.pdf`: assumptions, explanations, worked answers and proof notes.
- `lecture02-complete.zip`: all PDFs and a self-contained LaTeX source archive.
- `slide-index.md`: logical slide numbers, types and presentation page ranges.

There are **89 core slides**, **8 reserve slides introducing duality**, and
**8 optional mathematical proof/counterexample slides**: 105 logical slides total.

The revised sequence is:

1. Slides **1–11**: budget sets, existence and Marshallian demand homogeneity.
2. Slides **12–25**: Lagrangian and saddle prelude, followed by KKT conditions.
3. Slides **26–38**: the two complete KKT theorems and their proofs.
4. Slides **39–45**: Walras' law, convexity/uniqueness and solution strategy.
5. Slides **46–60**: solve Cobb–Douglas, substitutes, linear-plus-log utility
   and complements together, with questions followed by reveals.
6. Slides **61–70**: introduce indirect utility and discuss/prove its properties.
7. Slides **71–78**: general constrained envelope theorem, proof and application.
8. Slides **79–87**: prove Roy and recover demands in all four model families.


There is no “at the board” slide or student-facing staging instruction.
The first two budget propositions each reveal their own proof after the claim.
The title explicitly says Lecture 2; the warm-up graph shows utility levels
2, 4 and 6. Body line/paragraph spacing is increased throughout, with spaced
bullet lists for parallel points.
The core follows syllabus block 2. The tail of source Lecture 11 on expenditure
minimisation is marked as a preview of block 3, rather than required live coverage.

Topics: budget sets, existence, Marshallian demand, homogeneity, Walras' law,
convexity and uniqueness, indirect utility, KKT and complementary slackness,
interior and corner solutions, worked examples, envelopes, shadow values and Roy.
The reserve introduces Hicksian demand, expenditure properties and compensation.

## Build

```bash
./build.sh
```

Requirements: XeLaTeX, Beamer, fontspec, polyglossia, TikZ/pgfplots, DejaVu Sans.
The script compiles presentation, handout and notes twice. No network or secrets
are needed. Output PDFs are copied here; auxiliary files and logs stay in `build/`.

## Presentation choices

English text, NES colours and English logo, plain headings without shaded banners.
Questions have no generic Discuss label or timed exercise instructions. Semantic
steps appear successively. Claims and their short proofs are revealed in order.
Budget results come first; Walras' law, convexity/uniqueness and indirect-value
proofs follow the KKT block; the indirect-value section follows the four direct
optimisation examples. The value-continuity proof uses a fixed compact
expenditure-share simplex. Proof links have visible return links. The
presentation uses ordinary PDF pages for overlays, without JavaScript.

The saddle introduction comes **before KKT**. It uses the budget-only
Lagrangian ell(x,lambda) on x>=0, lambda>=0. The slides prove that a global
saddle implies feasibility, complementary slackness and optimality. They do
not exchange max and inf or assert a nonconcave saddle-existence theorem.
The later full Lagrangian adds quantity-bound multipliers for the KKT system;
a concave-KKT-to-budget-saddle proof is in the appendix.

No source-course HW5/HW6 notices were imported. The current Homework 1 covers
Lectures 1–2 and is due on 14 November 2026.

## Conventions and mathematical checks

m denotes wealth. D and H are demand correspondences; x and h denote vectors when
unique. v is indirect utility, e the expenditure function. The main KKT setup has
strictly positive prices and wealth. Existence, necessity and global sufficiency
are distinguished. Log utility is used only after interiority is established.
The envelope theorem is a general constrained smooth-branch version with
inequality and equality constraints. Its assumptions are C1 data and a C1
selection of optimal choices and KKT multipliers on an open parameter
neighbourhood. Its proof keeps all chain-rule terms before eliminating them.
Roy has a separate fixed-bundle proof: continuous utility, LNS, differentiable
v and a strictly positive wealth derivative suffice; direct utility and demand
need not be differentiable.

Worked examples include Cobb–Douglas, substitutes (corners and ties),
linear-plus-log utility a+4 log(1+q) (three price/income regimes), and complements
(a kink). All four are revisited after Roy. The quasilinear unit-price target
is q=3; the old square-root example has been replaced. Numerical budget checks, KKT
residuals, candidate optimality on budget grids, envelope/Roy derivatives and the
compensated example were independently checked during preparation.

See `SOURCE_NOTES.md` for source scope and corrections. The original NES-inspired
theme is reused from lecture 1. Museo Sans and Segoe UI are preferred if installed;
the tested build uses DejaVu Sans. No licensed fonts are bundled.

Optional reproducible numerical checks: `python3 verify-examples.py` (standard library only).
