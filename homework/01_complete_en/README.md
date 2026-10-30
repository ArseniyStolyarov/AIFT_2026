# Homework 1 — Preferences and consumer choice

Complete working edition for Lectures 1 and 2, in English and the course NES style.

- [Full student assignment](homework01.pdf?raw=true)
- [Part A: timed mock](part-a-mock.pdf?raw=true)
- [Part B: training](part-b-training.pdf?raw=true)
- [Instructor key](instructor-solutions.pdf?raw=true)
- [Complete source folder](homework01-complete.zip?raw=true)

- `homework01.pdf`: complete student assignment, Parts A and B.
- `part-a-mock.pdf`: only the formative 120-minute mock (100 diagnostic points).
- `part-b-training.pdf`: only the ordinary assessed, training-oriented set (100 points).
- `instructor-solutions.pdf`: complete key and suggested marking scheme.
- `homework01-complete.zip`: all PDFs, editable LaTeX and required assets, no password.

## Format

Part A contains the ten approved true/false statements, the trip and tutoring
problems, and two hypothetical trend-based short answers (maximum three sentences
each). These cases are not presented as verified news about real people.
Part A is diagnostic; its errors do not lower the final grade. It is a dense
120-minute exercise, as discussed during preparation.

Part B is a more routine instructional set with seven scaffolded exercises.
The existing assessment arrangement is preserved: B is the ordinary assessed
homework, while A is the formative mock. Three assessed homeworks contribute
equally to the course's 20% homework component. No deadline is assigned here.

## Edit and build

Edit `mock-true-false.tex`, `mock-problems.tex`, `mock-short-answers.tex` and
`training-body.tex`. Solutions are in `key-*.tex`. Run `bash build.sh` with
XeLaTeX and DejaVu Sans installed. No network is needed for compilation.
For Overleaf, upload the entire folder (keeping `assets/`), select XeLaTeX,
and choose `homework01.tex` or `instructor-solutions.tex` as the main file.
The instructor key is published separately. Send students only the student PDF;
the complete source archive also contains answers.

Earlier draft folders are retained for history; this directory is the current
complete assignment.
