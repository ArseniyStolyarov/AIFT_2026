#!/usr/bin/env bash
set -euo pipefail
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$project_dir"
mkdir -p build
for document in lecture02 handout instructor-notes; do
 xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$document.tex" > "build/$document.build.log" 2>&1
 xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$document.tex" >> "build/$document.build.log" 2>&1
 cp "build/$document.pdf" "$document.pdf"
done
