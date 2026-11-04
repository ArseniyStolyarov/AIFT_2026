# Seminar 2 — Consumer choice, KKT and Roy

An English problem sheet for the teaching assistant, in the established NES style.
No presentation is needed. Start with the short Roy recap, then solve at most
three multi-part problems:

1. Shifted product utility: log representation, corners, KKT, general interior value and Roy.
2. Linear plus shifted square root: three regimes, multipliers, indirect utility and Roy.
3. Minimum of two linear substitute indices: an auxiliary variable makes a linear
   constrained problem, with price regimes, kinks, boundary multiplicity and Roy.

[Student PDF](seminar02.pdf?raw=true) ·
[Instructor key](instructor-solutions.pdf?raw=true) ·
[Complete source folder](seminar02-complete.zip?raw=true)

The key suggests a 90-minute route. Optional calculations are part of the three
existing problems, not extra required problems. The sheet practises the skills
needed for Homework 1 with different functions/parameters. It adds no homework
or submission rule and changes no previously prepared course material.

## Build

Run `bash build.sh` with XeLaTeX and DejaVu Sans installed, or upload the entire
folder to Overleaf (keep `assets/`), select XeLaTeX and `seminar02.tex` as the main
file. Edit `seminar-problems.tex` for the questions and `instructor-solutions.tex`
for the key. The ZIP contains all editable files, both PDFs, the style and logo.
It includes answers; students should receive only `seminar02.pdf`.

## Verification

`python3 verify-examples.py` uses only the Python standard library. It checks
69 parameter cases against independent feasible budget grids, full KKT systems,
finite-difference Roy ratios and the nonunique boundary demand segments.
