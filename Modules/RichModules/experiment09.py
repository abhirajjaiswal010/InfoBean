from rich.prompt import Prompt

name = Prompt.ask("Enter your name")

print(name)
from rich.prompt import Prompt

choice = Prompt.ask(
    "Choose language",
    choices=["Python", "Java", "JavaScript"]
)