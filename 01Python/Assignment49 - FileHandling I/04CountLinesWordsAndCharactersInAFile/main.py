from pathlib import Path as path

base_dir = path(__file__).parent
file_path = base_dir / "article.txt"

n = int(input("Enter number of lines: "))

with open(file_path, "w+") as f:

    for i in range(n):

        line = input(f"Enter Line {i + 1}: ")

        f.write(line + "\n")

    f.seek(0)

    lines = f.readlines()

    total_lines = len(lines)
    total_words = 0
    total_characters = 0

    for line in lines:

        total_words += len(line.split())
        total_characters += len(line)

    print("\nFile Analysis\n")
  
    print(f"Total Lines      : {total_lines}")
    print(f"Total Words      : {total_words}")
    print(f"Total Characters : {total_characters}")