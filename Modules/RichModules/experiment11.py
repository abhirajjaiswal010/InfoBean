from rich import print
from rich.padding import Padding

text = Padding("Hello Python", 2)

print(text)


text = Padding(
    "Hello Python",
    (1, 4, 1, 4)
)

print(text)

from rich.console import Console
from rich.panel import Panel
from rich.padding import Padding

console = Console()

content = Padding(
    "Welcome to Python!",
    2
)

console.print(
    Panel(content, title="Message")
)