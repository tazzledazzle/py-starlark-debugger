#!/usr/bin/env sh
#mkdir starlark-debugger
#cd starlark-debugger

python3 -m venv venv
# shellcheck disable=SC3046
source venv/bin/activate
pip install bazel-starlark
