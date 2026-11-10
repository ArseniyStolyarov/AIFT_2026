# Microeconomics 3 — Duality and the Slutsky Equation

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.

## Downloads

- [Presentation with click-by-click reveals](lecture03.pdf?raw=true)
- [Handout: one final state per slide](handout.pdf?raw=true)
- [Russian instructor notes, answers and qualifications](instructor-notes.pdf?raw=true)
- [Entire folder: PDFs and editable LaTeX](lecture03-complete.zip?raw=true)
- [Slide index](slide-index.md)

There are **50 main slides and 15 appendix slides**: 65 handout pages,
251 presentation pages with reveals, plus Russian instructor notes.
The English presentation
continues Lecture 2 after Roy's identity. It does not repeat the saddle/KKT
proofs. Definitions, short proofs, examples and graph elements appear in stages.
The handout combines the reveal states into one page per logical slide.

## Route for two 90-minute classes

1. Slides 1–12: what we know, today's topics, why separate price effects;
   expenditure minimisation, a geometric construction, existence, no excess
   utility, homogeneity and convexity/uniqueness of Hicksian demand.
2. Slides 13–22: problems for working out together, followed by revealed
   solutions; duality and its proofs, a verification task and a checkpoint.
3. Slides 23–28: Shephard's statement and applications, the compensated law
   of demand with two explicitly numbered price/quantity scenarios, symmetry
   of cross-price derivatives, and a graphical substitution/income decomposition.
4. Slides 29–43: the chain-rule derivation of Slutsky, own and cross effects,
   quasilinear regimes, the potato story, Giffen and net/gross substitution.
5. Slides 44–50: reconstruct and test the Slutsky matrix from ordinary demand,
   reject an illustrative demand system, checkpoint and reading.

Question sets appear after duality (slide 22) and after the Giffen example
(slide 41). They cover price scaling, a numerical utility relabelling,
multiple optima, numerical Slutsky effects and
quasilinear corners. Each question appears on a separate click; answers are
only in the instructor notes. The concluding checkpoint is slide 48.

Appendix slides 51–59 contain the former slides 13–16, 28–29 and 33–35:
expenditure properties, detailed Shephard arguments, the full price Hessian,
negative semidefiniteness and the zero price direction. These were moved
without changing their content and are available for the seminar. Slides
60–65 retain CV/EV, finite Hicks versus Slutsky compensation, integrability,
three-good net complements and continuity. The teacher notes contain answers.

The first-half revision follows the lecturer's comments through former slide
36. Former slides 21–24 and the block from former slide 37 onward retain
their original content. The [slide index](slide-index.md) maps old to new
numbers for the next review. The two introductory graphs now have no numerical
utility formula or tick values, and each line appears in a separate reveal.

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

`python3 verify-examples.py` uses the standard library and checks **108**
parameter cases with independent feasible grids, finite differences,
Giffen KKT multipliers, duality, Slutsky and welfare.

The complete ZIP contains the three PDFs and all editable sources, style,
logo, build script, verification script and documentation under `lecture03/`.
It includes instructor answers.

The supplied materials and the changes made to their exposition are described
in [SOURCE_NOTES.md](SOURCE_NOTES.md).
