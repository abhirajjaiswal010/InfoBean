'''
Question:
Append two strings but remove duplicate adjacent characters.

Given two strings, append the second string to the first.
While appending, if two adjacent characters are the same,
keep only one occurrence.

The comparison must also consider the boundary between
the first and second strings.

Test Cases:

1. Input:
   s1 = "hello"
   s2 = "oworld"
   Output:
   heloworld

2. Input:
   s1 = "abc"
   s2 = "cde"
   Output:
   abcde

3. Input:
   s1 = "hello"
   s2 = "lo"
   Output:
   helo

4. Input:
   s1 = "aaa"
   s2 = "bbb"
   Output:
   ab

5. Input:
   s1 = "abc"
   s2 = "def"
   Output:
   abcdef

6. Input:
   s1 = "aa"
   s2 = "abb"
   Output:
   ab

7. Input:
   s1 = "python"
   s2 = "nnn"
   Output:
   python

8. Input:
   s1 = "abc"
   s2 = ""
   Output:
   abc

9. Input:
   s1 = ""
   s2 = "hello"
   Output:
   hello
'''



s1 = input("Enter The String 1: ")
s2 = input("Enter The String 2: ")

new = ""

# Process s1
if len(s1) > 0:
    new += s1[0]

for i in range(1, len(s1)):
    if s1[i] != s1[i - 1]:
        new += s1[i]

# Process s2
for i in range(len(s2)):
    if new == "":
        new += s2[i]

    elif new[-1] != s2[i]:
        new += s2[i]

print(new)