# Microeconomics 1 — Preferences, Choice and Utility

Arseniy Stolyarov, PhD in Economics, University of Wisconsin–Madison.
Artificial Intelligence and Financial Technologies, New Economic School, 2026/27.
Updated for the instructor's 27 October 2026 revisions.

## Documents

- `lecture01.pdf`: presentation with click-by-click Beamer overlays.
- `handout.pdf`: the same material with all reveals visible, one page per logical slide.
- `opening.pdf`: title and two states of the eight-tradition map.
- `instructor-notes.pdf`: English teaching notes, assumptions and exercise answers.
- `review-answers-ru.md`: Russian answers to the instructor's content questions.
- `slide-index.md`: current slide titles and presentation-PDF page ranges.

There are **54 main logical slides and 10 optional appendix slides**. The
presentation PDF has more pages because each reveal is a PDF page; the handout
has 64 pages. This is an ordinary PDF presentation, with no JavaScript dependency.
Advance once to reveal the next idea. Internal text links jump to proofs and back.

Course overview is logical slide 4. Homework, project, exam, office hours and the
seven-topic plan follow. The Amazon case has its own slide after that introduction
and a direct link from slide 3. Definitions of indifference and strict preference
are separate discovery slides. Monotonicity precedes the diagonal construction.

## Build

From this directory:

```bash
./build.sh
```

Requirements: XeLaTeX, Beamer, fontspec, polyglossia, TikZ, pgfplots, DejaVu Sans.
The script compiles `lecture01`, `handout`, `opening` and `instructor-notes` twice,
then copies the PDFs here. Temporary output is in `build/`. No network access,
credentials or running services are required to build.

## Pacing

Plan for two 90-minute sessions with the usual break. The expanded course
introduction and the legal discussion need time. Relations, rationality,
representation, ordinal meaning, indifference curves and budget geometry are the
first-block core. Formal proofs, the diagonal construction, separability and
quasilinearity are extension material if time permits. The instructor notes
identify those sections. Do not treat every appendix proof as required live coverage.

## Editing

- `lecture01.tex`: the full deck, with stable frame labels and overlay specifications.
- `handout.tex`: sets handout mode and includes the full deck.
- `title-slide.tex`: title, instructor and degree.
- `economic-map.tex`: eight schools and the course outline; no bottom note.
- `nesbeamer.sty`: reusable NES-inspired English theme, without shaded banners.
- `instructor-notes.tex`: English companion.

The source-handout attribution is retained in `SOURCE_NOTES.md` and the instructor
notes. Student reading is Varian, ninth edition, chapters 2–4; MWG (1995), chapter 1 and sections 3.B–3.C, is optional advanced reading.

## Visual identity

This is an original Beamer implementation of the supplied NES 2022 identity
manual. Brand colours are RGB 5/67/114 and 163/22/70. The unchanged English vector
logo is extracted from page 3 of the provided manual. The theme prefers Museo
Sans, then Segoe UI. Neither was supplied or installed, so the current build uses
DejaVu Sans. No fonts are downloaded or bundled without a licence.

## Legal example

The case is the **2023 FTC and states complaint against Amazon**, not an Amazon
lawsuit against eBay. The slide describes allegations, not a liability finding or
current case outcome. eBay is a rival-platform example in an explicitly
hypothetical fee calculation. The official FTC URL is linked. Live retrieval of
that URL from this machine was blocked by the outbound proxy (HTTP 403); no
successful current-source or procedural-status verification is claimed.

## Latest edits

Concrete restaurant dishes; corrected implication arrows; Yaromir and Zoya;
a discovery question about utility representation; a two-bliss-point graphic.
Requested answers and timing labels are removed from the student slides.
See `latest-review-answers-ru.md` for explanations and a 180-minute pacing guide.

## Latest addition: the full consumer picture

Logical slide 52 combines the budget and indifference curves. The exit ticket
is now slide 53 and reading slide 54. Homework releases are shifted to lecture
blocks 3, 5 and 7. Slides 36 and 47 explain their purpose before the formal steps.
The latest Russian explanations are in `explanations-36-47-ru.md`.

## Full speaker text

`lecture01-speaker-script.pdf` is the full Russian preparation manuscript for all
54 main slides and 10 appendix slides, including explanations, questions, answers
and seven figures. Its source is `lecture01-speaker-script.tex`; `build.sh` now
builds it too. Condorcet is slide 20. Use the current slide index after insertion.

## Curvature revision

The old slide 37 is removed. The old slides 42–43 are now slides 41–42:
convex-function definition, a question about convex preferences, linear and
exponential examples, a midpoint counterexample and quasiconcavity. Strict
convexity of preferences is retained on slide 40. The manuscript is updated.
