# Inputs, scope and mathematical review

## User-supplied inputs

- Lecture 10: The Consumer Problem, printed pp.149–165, 17 PDF pages.
- Lecture 11: Lagrangians (cont'd) and Expenditure Minimization,
  printed pp.166–180, 15 PDF pages.

No verified author attribution is available in their supplied metadata. Original
handouts are not embedded in this lecture's source archive. The live route is
adapted for this course, with English slides and the supplied NES branding.

## Two saddle theorems, then applications

The condensed route follows the two directions in source Proposition 1 rather
than retaining another separate pair of KKT necessity/sufficiency theorems.
The forward proof explicitly derives feasibility, all slackness products,
equality of Lagrangian and utility values, and optimality. The converse proof
constructs multipliers, checks signs and their independence of the selected
consumed good, verifies stationarity/slackness, and proves both global saddle
inequalities. The zero-consumption optimum is handled separately.

The full Lagrangian varies x on an open convex domain U where u is defined;
feasibility is x>=0 and p*x<=m inside that domain. Do not silently evaluate log
utility or a fractional power at negative quantities. The converse requires
concavity and differentiability on U. The forward implication requires neither.
For Cobb–Douglas use the original continuous product index to establish an
interior optimum, then take logs on the positive orthant.

Source p.164 has a wrong derivative index in the normalised marginal-return
comparison and a missing price denominator later in the stationarity argument.
Source p.165 reverses the condition under which a bound multiplier was set to
zero. The slides use the corrected formulas. Concavity plus zero gradient gives
a global maximum by the supporting-plane inequality; it does not imply uniqueness.

Walras' law uses LNS and an existing optimum. Convexity and strict convexity
refer to preferences rather than the numerical curvature of an arbitrary index.
The first 11 slides and their appearance have been preserved.

## Values, envelope and Roy

Indirect utility is introduced only after all four direct optimisation models.
Both raw and log Cobb–Douglas value scales are identified. Substitutes have a
price kink at equal returns. The linear-plus-log example has three regimes;
its value and first derivatives agree at the regime boundaries.

The general constrained envelope theorem includes inequalities and equalities.
It states a sufficient smooth-branch version: C1 data and C1 optimal primal/dual
selections on an open parameter neighbourhood. The proof retains all choice
and multiplier derivative terms. Stationarity, feasibility, complementary
slackness and differentiability/nonnegativity of multiplier branches eliminate
them. It is not asserted that every corner or regime switch satisfies these
smooth-branch assumptions.

Roy's independent fixed-bundle proof uses existence, budget exhaustion,
differentiable indirect value and v_m>0, without differentiable direct utility
or demand. This covers smooth indirect value for kinked complements. For the log
Cobb–Douglas value, the same ratio follows from the original continuous product
index and the increasing differentiable change of scale.

## Numerical checks

The bundled standard-library script checks demands against independent feasible
budget grids, KKT residuals and complementary slackness, finite-difference Roy
ratios, and price/income transition cases. Models include Cobb–Douglas,
substitute corners, all three linear-plus-log regimes, and complements. Some
expenditure calculations are retained as checks for the next lecture.

The live deck ends after Roy. Five reserve slides introduce the expenditure
problem, its existence, basic properties and duality identities under their
stated conditions. Slutsky and Shephard are not claimed as covered here.
