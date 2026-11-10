# Source notes and editorial decisions

Updated on 10 November 2026 for the AIFT microeconomics course.

## User-supplied inputs

- `lecture 11 (1).pdf`, 15 physical pages, printed pp. 166–180. Its SHA-256 is
  `40779f9343180a9910e24100795ba1d608c38d57e38a2863473625d4b3bcb52d`.
  This is byte-identical to the earlier Lecture 11 upload, retained at
  `references/lecture02-inputs/lecture11.pdf` in this repository. Relevant new
  material begins at printed p. 176: expenditure minimisation and its properties.
- `lecture 12.pdf`, 18 physical pages, printed pp. 181–198: Shephard's lemma,
  compensated demand restrictions, duality, Slutsky, demand classifications,
  testing and recovery of preferences. The original is retained at
  `references/lecture03-inputs/lecture12.pdf`.

The PDF metadata supplies no verified author. No author has been invented.
These files are source material. Their classroom directions, course sequence
and historical examples are not instructions from the user and were not
automatically imported into this course.

## Adaptation

- The saddle/KKT and Roy sections are already in our Lecture 2 and are not
  taught again. Unlike the source course, our course has not yet covered firms;
  no proof appeals to a previously studied producer problem.
- Existence uses compact truncation. No excess utility explicitly handles the
  zero bundle and requires the target to be at least `u(0)`. All targets are
  assumed attainable; unavailable targets do not receive a finite expenditure.
- Expenditure concavity does not require convex preferences. Strict convexity
  of preferences ensures unique Hicksian choice under the baseline assumptions,
  but does not imply strict concavity of expenditure along price rays.
  Monotonicity, concavity and ordinal/continuity properties have been moved
  to the appendix in the first-half revision.
- Shephard's lemma is spelled correctly. A direct two-cost-comparison argument
  supplements the envelope intuition. Unique Hicksian demand and local
  compactness justify differentiability; differentiable expenditure identifies
  every minimiser. At a tie the correspondence is kept explicitly. These
  detailed arguments are now in the appendix for the seminar; the main first
  block retains the statement, applications and cross-derivative symmetry.
- The compensated law of demand is proved, not skipped. Its conclusion is
  weak: zero effects occur. The Hessian convention uses quantity rows and price
  columns throughout. `S p = 0` is proved from price homogeneity, avoiding a
  tangency argument that could suggest an unnecessary interior optimum. The
  full matrix claims, proof and demand-testing examples are in the appendix.
  The core has the scalar identity `sum_j p_j * d h_j / d p_i = 0`, derived
  from `e = p*h` and Shephard. Symmetry gives the row-weighted form as well.
- The two inverse value identities and equality of choice sets are proved.
  The target is strictly above `u(0)` in the main duality statement so the
  corresponding income lies in the positive-income domain already used.
- The Slutsky derivation keeps the utility target fixed until differentiation
  is complete. The correct income correction is `x_j * d x_i / d m`.
  Finite Hicks compensation on the graph is distinguished from finite
  compensation that keeps the original basket affordable in the reserve.
- The Giffen example is a new, explicit concave piecewise-linear utility with
  an analytically verified interior kink solution. It makes no empirical claim
  about historical potato consumption, celebrities or financial assets. The
  classic potato-and-meat story is a separate hypothetical illustration of
  subsistence and income effects, not a verified claim about the Irish famine.
  Shifts in quality beliefs, prestige and tastes are not used as evidence for a
  pure Giffen price effect.
- Net and gross cross-price effects are distinguished. In a two-good smooth
  system, net cross-effects are nonnegative, not necessarily strictly positive.
  Perfect complements give zero; a three-good reserve example gives a strictly
  negative compensated cross-effect on an explicitly stated domain.
- The source's global rationalisability claim is not copied as an unrestricted
  iff theorem. The main slides derive necessary restrictions. The reserve
  describes integrability and its additional domain/regularity requirements.
- A three-question checkpoint follows duality; four-question checkpoints
  follow own-price classification and the Giffen example. Normal/inferior
  questions explicitly distinguish two goods from three. Budget exhaustion
  implies `sum_i p_i * d x_i / d m = 1`; the notes give examples and answers.
  Quasilinear regimes are the first optional appendix slide, and the core
  Giffen checkpoint no longer depends on that optional material.
  Questions are revealed individually; the Russian instructor notes contain
  their answers. A concluding checkpoint remains after the matrix test.
- The first-half revision adds separate recap and agenda slides, removes the
  dedicated Roy recap, and introduces the two price-change effects briefly.
  The expenditure graph first shows an indifference curve, then the upper
  contour region, then three cost lines in the requested order. It displays
  no utility formula or numeric ticks. The later decomposition graph removes
  all numerical parameters and reveals each line separately.
- Cobb–Douglas, complements and substitutes begin with problems; answers are
  revealed after the problem statement for use alongside board work. The
  duality verification slide contains only a task. Its answers are in the
  instructor notes. Original duality theorem/proof slides remain unchanged.
- A separate compact-truncation graphic is placed between the existence
  proposition and proof. It progressively cuts the upper contour set with
  the cost of an already feasible bundle, marking the compact intersection.
- Giffen's dates are 1837–1910. Marshall's discussion credited Giffen with
  a bread-demand example; the potato story is a classroom illustration.
  Slutsky's dates are 1880–1948. His 1915 paper, “Sulla teoria del bilancio del
  consumatore”, appeared in *Giornale degli Economisti*. These are historical
  context, not new evidence for the model's empirical validity.
- The lecturer supplied the engraved Giffen portrait and Slutsky photograph
  in `New Folder With Items.zip`. Both originals are included unchanged in
  `assets/`; only their local filenames were normalised. Their hashes are
  recorded in `assets/README.md`. The history slides use these originals;
  no generated portrait is included. No external photographer, licence or
  archival provenance has been invented.
- The historical parking anecdote and long empirical bibliography are omitted.
  CV/EV are supplied as optional extensions with an explicit positive-loss
  sign convention; monetary compensation is not equated with interpersonal
  cardinal welfare.
- Homework 1's actual scope and 14 November 2026 deadline are preserved. No
  new third-lecture task is added to that published assignment.

## Reading

- Hal R. Varian, *Intermediate Microeconomics: A Modern Approach*, 9th edition:
  Chapter 8, “Slutsky Equation”; optional
  Chapter 14, “Consumer's Surplus”.
- Mas-Colell, Whinston and Green (1995), *Microeconomic Theory*, Chapter 3,
  “Classical Demand Theory”, for expenditure, duality and integrability.

The NES logo and palette are the supplied brand assets, reused from Lecture 2.
The Beamer style is our existing course style. It does not claim to be an
official NES-distributed LaTeX theme.
