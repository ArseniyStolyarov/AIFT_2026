# Homework 1 — Preferences and consumer choice

Publication edition for Lectures 1 and 2, in English and the course NES style.
Deadline: **14 November 2026**.

- [Full student assignment](homework01.pdf?raw=true)
- [Part A: timed mock](part-a-mock.pdf?raw=true)
- [Part B: training](part-b-training.pdf?raw=true)
- [Instructor key](instructor-solutions.pdf?raw=true)
- [Complete source folder](homework01-complete.zip?raw=true)

- `homework01.pdf`: Parts A and B, followed by additional optional practice.
- `part-a-mock.pdf`: only the formative 120-minute mock (100 diagnostic points).
- `part-b-training.pdf`: only the ordinary assessed, training-oriented set (100 points).
- `instructor-solutions.pdf`: complete key and suggested marking scheme.
- `homework01-complete.zip`: all PDFs, editable LaTeX and required assets, no password.

## Format

Part A contains the ten approved true/false statements, the trip and tutoring
problems, and two hypothetical trend-based short answers (maximum three sentences
each). These cases are not presented as verified news about real people.
Part A has 50 points for the ten true/false claims (5 each), 15 and 25 for
the two problems, and 10 for the two short answers, totalling 100.
Part A is diagnostic; its errors do not lower the final grade. It is a dense
120-minute exercise, as discussed during preparation.

Part B contains three compulsory exercises: a preference checklist (30 points),
Cobb–Douglas (35) and corner solutions with KKT (35). Only one indifference
diagram is required in the checklist.

The other four blocks — representations/separability, budget geometry, perfect
complements and quasilinearity — appear at the end of the **same student PDF** as
additional optional practice. They have no points or submission requirement and
do not affect the 100-point Part B score. Their solutions are included at the
end of the same instructor key; there is no separate optional handout.
The existing assessment arrangement is preserved: B is the ordinary assessed
homework, while A is the formative mock. Three assessed homeworks contribute
equally to the course's 20% homework component. The deadline is **14 November 2026**.

## Edit and build

Edit `mock-true-false.tex`, `mock-problems.tex`, `mock-short-answers.tex` and
`training-body.tex`. Optional material is in `optional-body.tex`. Solutions are
in `key-*.tex`. Run `bash build.sh` with
XeLaTeX and DejaVu Sans installed. No network is needed for compilation.
For Overleaf, upload the entire folder (keeping `assets/`), select XeLaTeX,
and choose `homework01.tex` or `instructor-solutions.tex` as the main file.
The instructor key is published separately. Send students only the student PDF;
the complete source archive also contains answers.

Earlier draft folders are retained for history; this directory is the current
complete assignment.
