# Seminar 3 review — 12 November 2026

## Coverage

The worksheet applies Lecture 3's four-object square twice, using different
utility functions and direct optimisation before the derivative checks.
The key makes the parameter mapping explicit:
`e(p,v(p,m)) = m`, `v(p,e(p,ubar)) = ubar`, and `H(p,v(p,m)) = X(p,m)`.

The first problem makes the matrix work deferred from the lecture compulsory:
calculate the corrected Marshallian derivative matrix, check symmetry, `Sp=0`
and negative semidefiniteness, then prove the general theorem from Shephard,
price concavity of expenditure and homogeneity. The second shows that duality
survives without convex preferences while differentiability and uniqueness can fail at a tie.
It supplies a concrete example for the lecture's multiple-optima question.

## Audit against worked examples

Lecture 3 works through square-root Cobb–Douglas, Leontief, linear substitutes,
linear-plus-log quasilinearity and an offset minimum of two affine scores
for Giffen behaviour. Seminar 2 uses a shifted product, linear-plus-shifted-root
quasilinearity and another minimum of affine scores.

Neither complete consumer problem is reused here. The first new function is
a sum of weighted square roots, not the square root of a product; it has
strictly positive smooth demand. The second is a maximum with different
curvature in its two branches and a baseline only in the first branch.
That baseline changes preferences; it is not a common ordinal shift of the
entire utility index. At the chosen prices there are two income switches,
at `m=9/4` and `m=9`, corresponding to targets `3/2` and `3`.
It does not have the interval of tie optima from perfect
substitutes or the simultaneous thresholds from a min utility.

## Qualifications

- Positive prices and income; the nonnegative orthant. Targets are above 0
  in problem 1 and above the baseline 1 in problem 2, except where lower
  targets are explicitly examined.
- Strict concavity gives uniqueness in problem 1. Axis exclusion is justified
  by a square-root gain versus a first-order loss, not finite FOCs at zero.
- In the expenditure change of variables, the objective is strictly convex.
  The displayed positive KKT point is a global minimum.
- Roy and Shephard are used only in strict smooth regimes in problem 2.
  At a tie the whole demand set is listed, and value kinks are checked explicitly.
- A target constraint for a maximum is a union. Requiring both component
  thresholds would solve a different problem.
- Slutsky's Hicksian derivative is taken at a fixed target before the
  matching target is substituted.
- Matrix curvature is negative semidefinite; the price vector is a zero
  direction by homogeneity. The general result is proved, not inferred from
  the single numerical example.
- At prices `(4,1)` the maximum's branches have a tangential tie as functions
  of income. The income-only value is smooth, while price derivatives fail.
  This is the optional extension; the full solution does not incorrectly
  assert an income kink at every tie.

## Revised warm-up and stories

The five warm-up verdicts are **F, T, F, F, F**. All classifications are
strict, local and evaluated at the same prices and income. Exactly two goods
are assumed. Budget differentiation rules out two inferior goods; Slutsky
then rules out two Giffen goods. Cobb–Douglas supplies two normal goods.
A Leontief example shows that a negative cross-price derivative does not
imply inferiority.

The supplied Marshallian demand is `(12-m)/(2-p1)` at `p2=1`, in the open
region `1<p1<4/3`, `6p1<m<12`. Its own-price derivative is positive, its
income derivative is negative, and their Slutsky correction is zero.
The key rationalises it using `min{x1+x2, 2x1+1.5x2-6}`: on the budget,
one affine score decreases and the other increases, so their crossing is
the unique global optimum. This reuses the lecture's Giffen mechanism as
a short conceptual check with different coefficients, not as a repeated
full worked problem. Thirty new parameter cases independently verify
budget optimality, target-frontier costs and the compensated derivative.

The two full problems retain their utility functions, parameters and all
subquestions. The first now concerns a professor's two papers. Square-root
quality scores have diminishing returns and are not labelled acceptance
probabilities, since they are unbounded. The resource cost per research hour
is `p_i` and the only budget is the grant `m`. The second now concerns coffee
and cake at Glitch, the NES café. Goods are explicitly divisible serving
equivalents, and the baseline belongs only to the coffee branch.
