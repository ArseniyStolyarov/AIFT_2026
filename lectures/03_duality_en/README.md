# Microeconomics 3 — Duality and the Slutsky Equation

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.

## Downloads

- [Presentation with click-by-click reveals](lecture03.pdf?raw=true)
- [Handout: one final state per slide](handout.pdf?raw=true)
- [Russian instructor notes, answers and qualifications](instructor-notes.pdf?raw=true)
- [Entire folder: PDFs and editable LaTeX](lecture03-complete.zip?raw=true)
- [Slide index](slide-index.md)

There are **48 main slides and 21 appendix slides**: 69 handout pages,
267 presentation pages with reveals, plus Russian instructor notes.
The English presentation
continues Lecture 2 after Roy's identity. It does not repeat the saddle/KKT
proofs. Definitions, short proofs, examples and graph elements appear in stages.
The handout combines the reveal states into one page per logical slide.

## Route for two 90-minute classes

1. Slides 1–13: what we know, today's topics, why separate price effects;
   expenditure minimisation, a geometric construction, existence, no excess
   utility, homogeneity and convexity/uniqueness of Hicksian demand.
2. Slides 14–23: problems for working out together, followed by revealed
   solutions; duality and its proofs, a verification task and a checkpoint.
3. Slides 24–30: Shephard's statement and applications, the compensated law
   of demand with two explicitly numbered price/quantity scenarios, symmetry
   of cross-price derivatives, the zero price-weighted derivative identity,
   and a graphical substitution/income decomposition.
4. Slides 31–45: Slutsky's historical context, the chain-rule derivation,
   own and cross effects, normal/inferior questions, the potato story,
   Giffen and net/gross substitution.
5. Slides 46–48: concluding checkpoint, synthesis and reading.

Question sets appear after duality (slide 23), after own-price classification
(slide 36), and after the Giffen example (slide 44). They cover utility
relabelling, multiple optima, Slutsky signs, and whether goods can both be
normal or inferior. Each question appears on a separate click; answers are
only in the instructor notes. The concluding checkpoint is slide 46.

The appendix begins with quasilinear regimes (slide 49), only if time permits.
Slides 50–58 contain deferred expenditure properties, detailed Shephard
arguments and the full price Hessian. Slides 59–63 contain the two-good
matrix implication, construction/testing of the Slutsky matrix and its
examples. No matrix block remains in the core lecture. Slides 64–69 retain
CV/EV, finite compensation, integrability, three-good net complements and
continuity. The deferred frames retain their original content.

The [slide index](slide-index.md) maps the previous version to current numbers.
Slide 9 draws the compact truncation before its formal proof: upper contour
set, reference bundle, budget cap, compact intersection. The introductory
graphs have no numerical utility formula or tick values; paths themselves,
not only their captions, appear in stages.

## Historical portraits

The Giffen and Slutsky slides contain short historical notes. The lecturer
provided an engraved Giffen portrait and a Slutsky photograph inline in chat,
but their original image files are not yet available in the cloud workspace.
The generated substitutes have been removed. Place the originals at
`assets/giffen-portrait.png` and `assets/slutsky-portrait.jpg`; the build then
includes them automatically. The current PDF contains the historical text
without a substitute portrait. See `assets/README.md` for provenance status.

## Mathematical conventions

`X` and `H` denote demand correspondences; lowercase `x` and `h` are used for
unique demand. The baseline domain is the nonnegative orthant, utility is
continuous, prices strictly positive and the target attainable and at least
`u(0)`. Duality adds LNS. Derivative results state their additional conditions;
the price Hessian results use locally C2 expenditure. Kinks and regime
boundaries are not differentiated automatically.

The matrix convention is `S_ij = d h_i / d p_j`, so the observable correction
is `S = D_p x + (D_m x) x^T`. Own compensated effects are weakly nonpositive,
and common price scaling gives `S p = 0`.
Integrability is presented as an extension with additional domain/regularity
conditions, not an unconditional global converse.

The three-good logarithmic example in the reserve explicitly changes its
domain to positive quantities of the first two goods. It is justified directly,
without invoking continuity at the origin. Homework 1 remains the published
assignment on Lectures 1–2, due **14 November 2026**.

## Build and check

Run `bash build.sh`. It builds all three PDFs twice with XeLaTeX. Dependencies
are the same as Lecture 2: Beamer, fontspec, polyglossia, TikZ/pgfplots and
DejaVu Sans (fallback when Museo Sans and Segoe UI are unavailable). For
Overleaf, upload the whole source folder, keep `assets/`, choose XeLaTeX and
select `lecture03.tex`, `handout.tex` or `instructor-notes.tex` as the main file.

`python3 verify-examples.py` uses the standard library and checks **110**
parameter cases with independent feasible grids, finite differences,
Giffen KKT multipliers, duality, Slutsky, welfare, compact truncation and a
three-good example with two inferior goods.

The complete ZIP contains the three PDFs and all editable sources, style,
logo, build script, verification script and documentation under `lecture03/`.
It includes instructor answers.

The supplied materials and the changes made to their exposition are described
in [SOURCE_NOTES.md](SOURCE_NOTES.md).
