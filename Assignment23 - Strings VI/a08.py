'''
Docstring for Assignment23 - String VI.a07
Intelligent Search Query Compressor

A search engine company wants to compress user queries.

Write a Python program to compress a search query using the following rules:

Rules:
• Count the frequency of each character
• Display characters in alphabetical order
• Ignore spaces
• Treat uppercase and lowercase letters as the same (case-insensitive)

Input:
Google Search

Output:
a1c1e2g2h1l1o2r1s1t1
'''

n = input("Enter : ").lower()

new = ""

# Spaces ko ignore karke saare characters ek string mein lao
for word in n.split():

    for i in word:
        new += i

freq = {}

# Har character ki frequency count karo
for i in new:

    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

ans = ""

# Characters ko alphabetical order mein process karo
for i in sorted(freq):

    # Character + uski frequency add karo
    ans += i + str(freq[i])

print(ans)


        
        