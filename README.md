# Python Starlark Debugger
Starlark Debugger is a simple command-line tool for debugging Starlark scripts. It allows you to set breakpoints, step through the code, inspect variables, and control the execution flow of your Starlark scripts.

## Features

- Set breakpoints to pause execution at specific lines.
- Step through the script line by line.
- Inspect variables during execution.
- Continue execution until the next breakpoint.
- Simple command-line interface for debugging.

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/starlark-debugger.git
cd starlark-debugger
```

## Usage

1. **Prepare your Starlark script:**

   Create a Starlark script file (e.g., `example.bzl`) that you want to debug.

   ```python
   # example.bzl
   a = 1
   b = 2
   c = a + b
   print(c)
   ```

2. **Run the debugger:**

   Execute the debugger with the path to your Starlark script:

   ```bash
   python starlark_debugger.py example.bzl
   ```

3. **Debugger commands:**

   While the script is paused at a breakpoint, you can use the following commands:

   - `c`: Continue execution until the next breakpoint.
   - `n`: Step to the next line.
   - `b <line_number>`: Set a breakpoint at the specified line number.
   - `p <variable_name>`: Print the value of the specified variable.
   - `q`: Quit the debugger.

## Example

```bash
$ python starlark_debugger.py example.bzl
Breakpoint at line 2: a = 1
(debugger) n
Breakpoint at line 3: b = 2
(debugger) n
Breakpoint at line 4: c = a + b
(debugger) p a
1
(debugger) p b
2
(debugger) c
3
```

## Limitations

- This debugger is a basic implementation and does not cover the full Starlark language specification.
- For advanced features and full support for Starlark, consider using official tools provided by Bazel.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
