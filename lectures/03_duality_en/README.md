# Microeconomics 3 — Duality, Slutsky and Revealed Preference

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.

## Downloads

- [Presentation with click-by-click reveals](lecture03.pdf?raw=true)
- [Handout: one final state per slide](handout.pdf?raw=true)
- [Russian instructor notes, answers and qualifications](instructor-notes.pdf?raw=true)
- [Entire folder: PDFs and editable LaTeX](lecture03-complete.zip?raw=true)
- [Slide index](slide-index.md)

There are **60 main slides and 7 reserve slides**: 67 handout pages, 253
presentation pages with reveals, and 13 pages of Russian instructor notes.
The English presentation
continues Lecture 2 after Roy's identity. It does not repeat the saddle/KKT
proofs. Definitions, short proofs, examples and graph elements appear in stages.
The handout combines the reveal states into one page per logical slide.

## Route for two 90-minute classes

1. Slides 1–20: expenditure minimisation, existence, no excess utility,
   homogeneity, convexity/uniqueness of Hicksian demand, monotonicity and
   concavity of expenditure; Cobb–Douglas, complements and substitutes.
2. Slides 21–34: both duality identities, equality of demand correspondences,
   Shephard's lemma with a direct proof, the compensated law of demand,
   symmetry, negative semidefiniteness and the zero price direction.
3. Slides 35–48: a numerical substitution/income diagram, the chain-rule
   derivation of Slutsky, own and cross effects, quasilinear regimes, an explicit
   Giffen example, and net versus gross substitution.
4. Slides 49–60: reconstruct and test the Slutsky matrix from ordinary demand,
   reject an illustrative demand system, test two observed budgets using
   revealed preference, checkpoint and reading.

The reserve covers CV/EV, finite Hicks versus Slutsky compensation,
integrability, a three-observation GARP cycle, genuine net complements with
three goods, and continuity of expenditure. The teacher notes suggest pacing
and contain answers to every open question.

## Mathematical conventions

`X` and `H` denote demand correspondences; lowercase `x` and `h` are used for
unique demand. The baseline domain is the nonnegative orthant, utility is
continuous, prices strictly positive and the target attainable and at least
`u(0)`. Duality adds LNS. Derivative results state their additional conditions;
the price Hessian results use locally C2 expenditure. Kinks and regime
boundaries are not differentiated automatically.

The matrix convention is `S_ij = d h_i / d p_j`, so the observable correction
is `S = D_p x + (D_m x) x^T`. Own compensated effects are weakly nonpositive,
and common price scaling gives `S p = 0`. WARP is stated in the budget
formulation allowing indifferent optimal choices: one strict affordability
comparison is needed for a pairwise contradiction. Longer cycles require GARP.
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
parameter/data cases with independent feasible grids, finite differences,
Giffen KKT multipliers, duality, Slutsky, revealed preference and welfare.

The complete ZIP contains the three PDFs and all editable sources, style,
logo, build script, verification script and documentation under `lecture03/`.
It includes instructor answers.

The supplied materials and the changes made to their exposition are described
in [SOURCE_NOTES.md](SOURCE_NOTES.md).
