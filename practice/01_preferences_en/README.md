# Seminar and Homework 1 — Preferences and utility

English materials in the established NES course style. Based on Lecture 1:
relations, rationality, utility representation, continuity, convexity,
monotonicity, local nonsatiation, choice correspondences and budget geometry.
No Lagrangian, KKT or demand calculus is required.

## Student files

- [Seminar worksheet: questions only](seminar-worksheet.pdf?raw=true)
- [Homework 1: both parts](homework01.pdf?raw=true)
- [Part A: formative 120-minute mock](homework01-mock.pdf?raw=true)
- [Part B: assessed problems](homework01-assessed.pdf?raw=true)
- [Student PDF bundle — no answers](preferences01-student.zip?raw=true)

## Teaching files

- [Seminar presentation: click-by-click answers](seminar01.pdf?raw=true)
- [Seminar handout: all answers visible](seminar-handout.pdf?raw=true)
- [Password-protected instructor bundle](preferences01-instructor.zip?raw=true)

The instructor archive contains all PDFs and editable LaTeX, including complete
solutions and marking guidance. The password is delivered privately in the
course-preparation chat, not committed to this public repository. Use an AES-ZIP
compatible extractor, such as 7-Zip or Keka. The public presentation reveals
**seminar** answers, not homework answers. Do not send it as the pre-class worksheet.

## Format and timing

The seminar has a 90-minute core route and a reserve exercise. Its 19 logical
slides have separate question and answer states (35 PDF pages).

Part A is a topical mock of the exam format: 120 minutes, true/false with
justification, problems and one qualitative question. It covers Lecture 1, not
the entire final-exam syllabus. Its score out of 100 is diagnostic; mistakes do
not reduce the final course grade. The suggested closed-resource sitting is a
practice recommendation, not a new rule for permitted materials at the final.

Part B has four harder assessed problems, out of 100. Only this score enters
Homework 1's assessed grade. The three homeworks are equally weighted within
the 20% homework component. Both parts are handwritten. AI use in assessed work
must be disclosed and all work explainable by the student.

This set is prepared in advance. The revised release schedule remains blocks
3/5/7; no deadline has been assigned here. The instructor can supplement this
topical set with subsequent material before release.

## Build

```bash
./build.sh
```

Requires XeLaTeX, Beamer, TikZ/pgfplots, fontspec, polyglossia and DejaVu fonts.
No network or credentials are required. Public checkouts build student documents
and seminar slides; instructor solution sources are inside the protected archive.
After extracting it into this directory, the same command also builds solutions.
All problem wording is in `seminar-problems.tex`, `homework-mock-body.tex`, and
`homework-assessed-body.tex`. Update the archives separately after editing.

## Mathematical checks

The answer keys include proofs rather than just labels. Important distinctions:
a closed preference graph need not be transitive; lexicographic preferences on
the square are strictly convex but lack a real-valued representation; convex
preferences need not admit a concave representation; even a continuous strict
preference model may have a bliss point. Counterexamples name their domain and
check theorem hypotheses. All PDFs were compiled twice and inspected for TeX
errors, missing glyphs and overfull boxes; representative pages were rendered
for visual inspection.
