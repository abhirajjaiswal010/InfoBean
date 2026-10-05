from pathlib import Path as path

base_dir = path(__file__).parent
file_path = base_dir / "paragraph.txt"

n = int(input("Enter Number Of lines : "))
with open(file_path, "w+") as f:
    for i in range(n):
        line = input(f"Enter Line {i+1}th :")
        f.write(line + "\n")

    f.seek(0)

    para = f.readlines()

    total_vowels = 0
    total_consonants = 0

    for line in para:

        for ch in line.lower():

            if ch!=" " and ch not in "!@#$%^&*()_+=*" and ch not in "0123456789":
                if ch in "aeiou":
                    total_vowels += 1
                else:
                    total_consonants += 1


print(f"""Total Vowels: {total_vowels}
Total Consonants:{total_consonants}""")
