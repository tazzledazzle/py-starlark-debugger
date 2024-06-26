# BUILD

py_binary(
    name = "starlark_debugger",
    srcs = ["starlark_debugger.py"],
    main = "starlark_debugger.py",
)

load("//bazel:debugger.bzl", "debugger")

debugger(
    name = "run_debugger",
    script = ":starlark_debugger.bzl",
)
