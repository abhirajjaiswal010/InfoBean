from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(
    Panel("Welcome to Python!", title="Message")
)
console.print(
    Panel(
        "Program executed successfully!",
        title="Success",
        border_style="green"
    )
)