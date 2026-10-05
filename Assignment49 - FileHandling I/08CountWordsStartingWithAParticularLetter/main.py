from pathlib import Path as path
import string


base_dir = path(__file__).parent
file_path = base_dir / "article.txt"

n = input("Enter Your Para: ")

with open(file_path, "w+") as f:

    f.write(n)

    f.seek(0)

    line = f.read()

    start_char = input("Enter Character: ")

    

    for word in line.split():

        word = word.strip(string.punctuation)

        if word[0].lower() == start_char.lower():
            print(word)

