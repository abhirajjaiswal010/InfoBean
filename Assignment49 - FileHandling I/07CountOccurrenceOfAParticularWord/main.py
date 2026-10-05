from pathlib import Path as path
import string


base_dir = path(__file__).parent
file_path = base_dir / "article.txt"

n = input("Enter Your Para: ")

with open(file_path, "w+") as f:

    f.write(n)

    f.seek(0)

    line = f.read()

    search_word = input("Enter word to search: ")

    count = 0

    for word in line.split():

        word = word.strip(string.punctuation)

        if word.lower() == search_word.lower():
            count += 1

print(f"\n{search_word} occurs {count} times in the file.")