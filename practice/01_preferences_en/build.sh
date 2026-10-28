#!/usr/bin/env bash
set -euo pipefail
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$project_dir"
mkdir -p build
# Instructor source files may be absent in a public/student checkout.
for document in seminar-worksheet seminar-solutions homework01 homework01-mock homework01-assessed homework01-solutions; do
 [[ -f "$document.tex" ]] || continue
 xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$document.tex" > "build/$document.build.log" 2>&1
 xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$document.tex" >> "build/$document.build.log" 2>&1
 cp "build/$document.pdf" "$document.pdf"
done
