#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p build
for document in true-false solutions; do
 for pass in 1 2; do
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=build "$document.tex" > "build/$document.build.log" 2>&1
 done
 cp "build/$document.pdf" "$document.pdf"
done
