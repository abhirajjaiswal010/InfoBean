'''
Docstring for a03
 Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java   is   easy

Output: Cleaned Message: Java is easy
'''

n = input("Enter The Message : ")

s = ""
i = 0
space = False

while i < len(n):

    if n[i] != " ": #agar char hai
        if space and s != "":
            s += " "
        s += n[i]
        space = False
    else:
        if s != "":
            space = True

    i += 1

print("Cleaned Message:", s)