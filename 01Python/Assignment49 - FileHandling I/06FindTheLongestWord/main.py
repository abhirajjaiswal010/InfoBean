from pathlib import Path as path

import string

base_dir = path(__file__).parent
file_path = base_dir / "article.txt"

n = input("Enter Your Para : ")

with open(file_path, "w+") as f:
    f.write(n)
    f.seek(0)

    line = f.read()
    print(line)

    high_word_len = ""

    for word in line.split():
        word = word.strip(string.punctuation)

        if len(word) > len(high_word_len):
            high_word_len = word

print(f"\n Longest Word  : {high_word_len}")
print(f"\n Length        : {len(high_word_len)}")
