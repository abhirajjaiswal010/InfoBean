# remove occurrences of a word in a string


# Input:
#* Enter The String : java is powerful and java is popular
#* Enter The Word : java

#^ Output:
# is powerful and is popular

s = input("Enter the String: ")
word = input("Enter the Word: ")

new = ""
k = 0

for i in range(len(s)):

    if k > 0: # word ko skip kar rha hai 
        k -= 1
        continue

    match = True
    if i + len(word) <= len(s):
        for j in range(len(word)):
            if s[i + j] != word[j]:
                match = False
                break
    else:
        match = False

    if match:
        k = len(word) - 1
    else:
        new += s[i]

print(new)