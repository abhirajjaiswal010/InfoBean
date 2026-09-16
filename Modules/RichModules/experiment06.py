from rich.console import Console
from rich.syntax import Syntax

console = Console()

code = """
def add(a, b):
    return a + b

print(add(10, 20))
"""

syntax = Syntax(code, "python", theme="monokai")

console.print(syntax)