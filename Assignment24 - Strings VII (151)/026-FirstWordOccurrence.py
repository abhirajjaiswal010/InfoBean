# 26. Find the first occurrence of a word in a string.

# Write a Python program to find the index of the first occurrence of a given word (substring) in a string.

# If the word is not present in the string, print -1.


# Input:
#^ Enter The String : java is powerful and java is simple
#^ Enter The Word : java
#* output : 0

s = input("Enter the String: ")
word = input("Enter the Word: ")


idx = -1

possiblePositions = len(s) - len(word) + 1

for i in range(possiblePositions):

    match = True

    for j in range(len(word)):

        if s[i + j] != word[j]:
            match = False
            break

    if match:
        idx = i
        break

print(idx)