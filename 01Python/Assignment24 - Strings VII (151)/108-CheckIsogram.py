# Problem: Check Isogram
#
# An isogram is a word or sentence in which no letter appears
# more than once.
#
# Given a string s, return True if the string is an isogram,
# otherwise return False.
#
# The comparison should be case-insensitive.
# Ignore spaces and hyphens if present.
#
# Example 1:
# Input: s = "Machine"
# Output: True
# Explanation: Every letter appears only once.
#
# Example 2:
# Input: s = "Programming"
# Output: False
# Explanation: The letter 'r' and 'g' appear more than once.
#
# Example 3:
# Input: s = "isogram"
# Output: True
#
# Example 4:
# Input: s = "Alphabet"
# Output: False
# Explanation: The letter 'a' appears more than once.
#
# Constraints:
# 1 <= len(s) <= 1000
# s contains English letters, spaces, and hyphens.

# Approach:
# 1. Convert the string into lowercase.
# 2. Ignore spaces and hyphens.
# 3. Pick one character at a time.
# 4. Compare it with every character after it.
# 5. If a duplicate is found, return False.
# 6. If no duplicates exist, return True.

def approach01(s):
    s=s.lower()
    for i in range(len(s)):
        if s[i]==" " or s[i]=="-":
            continue
        
        for j in range(i + 1, len(s)):

            if s[j] == ' ' or s[j] == '-':
                continue

            if s[i] == s[j]:
                return False

    return True

s=input("Enter  :")
print(approach01(s))

def approach02(s):
    seen=set()

    for ch in s.lower():
        if ch==" " or ch=="-":
            continue
        if ch in seen:
            return False
        
        seen.add(ch)
    
    return True


            

            
        

