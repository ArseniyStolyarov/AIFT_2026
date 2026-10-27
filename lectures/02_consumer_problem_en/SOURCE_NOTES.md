# Sources and qualifications

## Supplied inputs

- `lecture 10.pdf`: “Lecture 10: The Consumer Problem”, 17 PDF pages,
  printed pages 149–165.
- `lecture 11.pdf`: “Lecture 11: Lagrangians (cont'd) and Expenditure Minimization”,
  15 PDF pages, printed pages 166–180.

Author information is not identified in the supplied headers or metadata. No
unverified author attribution is added. The teaching sequence and standard
results are adapted; diagrams, numeric examples and notes are prepared for this
course. Source files themselves are not redistributed in the archive.

## Syllabus placement

The core covers block 2: utility maximisation, Marshallian demand, indirect
utility, constrained optimisation and Roy. Expenditure minimisation and the
Hicksian side of duality, from the end of input Lecture 11, are retained in a
separate reserve section for block 3. Slutsky and Shephard are not claimed as
covered by this deck.

Assigned student reading is Varian, Intermediate Microeconomics: A Modern
Approach, ninth edition (2014), chapters 5 Choice and 6 Demand; optionally MWG,
Microeconomic Theory (1995), section 3.D The Utility Maximization Problem and
the Mathematical Appendix on constrained optimisation. The source handouts are
adaptation inputs, not substituted for the textbook assignment.

## Corrections and conditions

- Existence requires a nonempty compact budget and continuous utility. Uniqueness
  is a separate result using strict convex preferences, not convex utility.
- KKT necessity is stated with smoothness near the candidate and the constraint
  qualification. Positive prices and wealth make the active linear gradients
  independent, including at corners. Differentiability is not silently assumed
  at a minimum kink or a zero logarithm/square-root boundary.
- The log Cobb–Douglas representation is used after establishing positivity
  using the original continuous product utility. No restriction that the sum of
  positive exponents be at most one is needed for its demand solution.
- Marginal conditions retain the correct price indices and complementary
  slackness sets a bound multiplier to zero when its quantity is positive.
  Several such indices/inequalities are mistyped in the handouts.
- Quasiconcavity alone is not a global first-order sufficiency theorem. A shifted
  cubic supplies a stationary KKT nonmaximum. Concavity supplies the sufficient
  condition used here; global saddle inequalities are kept distinct.
- A binding budget can have zero multiplier, even with strictly increasing
  preferences. This is distinct from Roy's strictly positive v_m assumption.
- Roy's optional direct proof uses the supporting budget q*x*, so it neither
  assumes differentiable demand nor assumes uniqueness to prove uniqueness.
- Expenditure targets must be attainable. No excess utility is stated only for
  targets at least u(0). The preview's duality identities use targets above the
  baseline to stay inside the positive-wealth core; the zero-wealth extension
  is discussed explicitly in the notes.
- Expenditure continuity is restricted to the attainable target domain under
  the stated continuity/LNS assumptions. An infeasible target does not have a
  finite expenditure value merely because a formula was written down.
- Money-metric welfare measures do not remove the need for normative assumptions
  when aggregating effects across people.

## Newly prepared worked examples

- Cobb–Douglas: alpha=1/2, prices (2,1), wealth 12 -> quantities (3,6);
  first price 3 -> quantities (2,6).
- Substitutes: 2*x1+x2 at prices (3,1), wealth 12 -> (0,12), lambda=1,
  mu=(1,0). At prices (2,1), the entire budget line is optimal.
- Complements: min(x1,x2) -> equal quantities m/(p1+p2).
- Quasilinearity: a+4*sqrt(y), unit prices -> y=min(m,4), with distinct boundary
  and positive-numeraire multiplier regimes.
- Compensated Cobb–Douglas: raise first price from 1 to 2, initial wealth 8 and
  raw utility 4 -> compensated quantities (2*sqrt(2),4*sqrt(2)), expenditure
  8*sqrt(2), compensation approximately 3.31.
