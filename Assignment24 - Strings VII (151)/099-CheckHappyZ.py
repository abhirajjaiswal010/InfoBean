# Check Happy String
# Question Statement

# Given a string s, check whether it is a happy string.

# A string is considered happy if no two adjacent characters are the same.

# Return True if the string is happy; otherwise return False.

'''
Docstring for 099-CheckHappyZ
Examples
Input:  "abcde"
Output: True
Input:  "aabbc"
Output: False
Input:  "abca"
Output: True
Input:  "aabb"
Output: False
'''
s = input("Enter the string: ")

happy = True

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        happy = False
        break

print(happy)