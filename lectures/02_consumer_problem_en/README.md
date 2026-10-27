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

There are **49 core slides**, **8 reserve slides introducing duality**, and
**12 optional mathematical proof/counterexample slides**: 69 logical slides total.
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
steps appear successively. Proof links have visible return links. The presentation
uses ordinary PDF pages for overlays, with no JavaScript requirement.

No source-course HW5/HW6 notices were imported. In this course HW1 is released
after block 3, matching the lecturer's updated 3/5/7 schedule.

## Conventions and mathematical checks

m denotes wealth. D and H are demand correspondences; x and h denote vectors when
unique. v is indirect utility, e the expenditure function. The main KKT setup has
strictly positive prices and wealth. Existence, necessity and global sufficiency
are distinguished. Log utility is used only after interiority is established.
Roy requires differentiable v and a strictly positive wealth derivative.

Worked examples include Cobb–Douglas, substitutes (corners and ties), complements
(a kink) and quasilinearity (a binding numeraire). Numerical budget checks, KKT
residuals, candidate optimality on budget grids, envelope/Roy derivatives and the
compensated example were independently checked during preparation.

See `SOURCE_NOTES.md` for source scope and corrections. The original NES-inspired
theme is reused from lecture 1. Museo Sans and Segoe UI are preferred if installed;
the tested build uses DejaVu Sans. No licensed fonts are bundled.

Optional reproducible numerical checks: `python3 verify-examples.py` (standard library only).
