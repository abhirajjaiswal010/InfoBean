from rich.console import Console
from rich.table import Table

console = Console()

table = Table()

table.add_column("Name")
table.add_column("Age")
table.add_column("Course")

table.add_row("Abhiraj", "21", "B.Tech CSE")
table.add_row("Rahul", "22", "BCA")
table.add_row("Aman", "21", "B.Tech")

console.print(table)