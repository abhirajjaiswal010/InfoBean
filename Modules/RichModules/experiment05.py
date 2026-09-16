from rich.console import Console
from rich.markdown import Markdown

console = Console()

text = """
# Python

Python is a **high-level programming language**.

- Easy to learn
- Powerful
- Versatile
"""

console.print(Markdown(text))
