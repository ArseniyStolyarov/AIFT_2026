#!/usr/bin/env bash
set -euo pipefail
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$project_dir"
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build lecture01-speaker-script.tex > build/speaker-script.build.log 2>&1
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build lecture01-speaker-script.tex >> build/speaker-script.build.log 2>&1
cp build/lecture01-speaker-script.pdf lecture01-speaker-script.pdf
