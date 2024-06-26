# bazel/debugger.bzl

def _debug_impl(ctx):
    script_path = ctx.file.script.path
    ctx.actions.run(
        inputs = [ctx.file.script],
        outputs = [],
        executable = ctx.executable._debugger,
        arguments = [script_path],
    )

debugger = rule(
    implementation = _debug_impl,
    attrs = {
        "script": attr.label(allow_single_file = True),
        "_debugger": attr.label(
            allow_single_file = True,
            executable = True,
            default = "//:starlark_debugger",
        ),
    },
)
