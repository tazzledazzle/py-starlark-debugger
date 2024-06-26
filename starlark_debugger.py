# starlark_debugger.py

import sys


class StarlarkDebugger:
    def __init__(self, script_path):
        self.script_contents = None
        self.script_path = script_path
        self.breakpoints = set()
        self.variables = {}
        self.current_line = 0

    def load_script(self):
        with open(self.script_path, 'r') as file:
            self.script_contents = file.readlines()

    def run(self):
        self.load_script()
        self.current_line = 0
        while self.current_line < len(self.script_contents):
            line = self.script_contents[self.current_line].strip()
            if self.current_line in self.breakpoints:
                self.debug_prompt(line)
            else:
                self.execute_line(line)
            self.current_line += 1

    def execute_line(self, line):
        exec(line, self.variables)

    def debug_prompt(self, line):
        print(f"Breakpoint at line {self.current_line}: {line}")
        while True:
            command = input("(debugger) ").strip()
            if command == 'c':  # Continue
                break
            elif command == 'n':  # Next
                self.current_line += 1
                break
            elif command.startswith('b'):  # Set breakpoint
                _, line_num = command.split()
                self.breakpoints.add(int(line_num))
            elif command.startswith('p'):  # Print variable
                _, var_name = command.split()
                print(self.variables.get(var_name, "Variable not found"))
            elif command == 'q':  # Quit
                sys.exit(0)


if __name__ == "__main__":
    script_path = sys.argv[1]
    debugger = StarlarkDebugger(script_path)
    debugger.run()
