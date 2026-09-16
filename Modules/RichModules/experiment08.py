from rich.tree import Tree
from rich.console import Console

tree = Tree("Python")

tree.add("Basics")
tree.add("Functions")
tree.add("OOP")

console = Console()
console.print(tree)
