# Problem: Smallest Lexicographical Substring
#
# Given a string s, find the lexicographically smallest substring
# of length k.
#
# A substring is a contiguous sequence of characters taken from
# the original string.
#
# Lexicographical order means dictionary order, where characters
# are compared from left to right.
#
# If two substrings have different first characters, the substring
# with the smaller character is lexicographically smaller.
#
# If their first characters are equal, compare the next characters,
# and continue until a difference is found.
#
# If all compared characters are equal, the shorter string is
# considered lexicographically smaller.
#
# Return the smallest substring of length k.
#
# --------------------------------------------------
# Example 1:
#
# Input:
# s = "welcometocode"
# k = 3
#
# Output:
# "cod"
#
# Explanation:
# All possible substrings of length 3 are compared.
# "cod" is lexicographically smaller than all other substrings.
#
# --------------------------------------------------
# Example 2:
#
# Input:
# s = "banana"
# k = 2
#
# Output:
# "an"
#
# Explanation:
# Substrings of length 2:
# "ba", "an", "na", "an", "na"
#
# The smallest substring is "an".
#
# --------------------------------------------------
# Example 3:
#
# Input:
# s = "abcde"
# k = 1
#
# Output:
# "a"
#
# Explanation:
# Every individual character is a substring of length 1.
# "a" is the smallest character.
#
# --------------------------------------------------
# Example 4:
#
# Input:
# s = "zxyabc"
# k = 3
#
# Output:
# "abc"
#
# Explanation:
# The smallest substring of length 3 is "abc".
#
# --------------------------------------------------
# Example 5:
#
# Input:
# s = "dcba"
# k = 2
#
# Output:
# "ba"
#
# Explanation:
# Possible substrings:
# "dc", "cb", "ba"
#
# "ba" is lexicographically smallest.
#
# --------------------------------------------------
# Example 6:
#
# Input:
# s = "aaaaa"
# k = 3
#
# Output:
# "aaa"
#
# Explanation:
# Every substring of length 3 is identical.
#
# --------------------------------------------------
# Example 7:
#
# Input:
# s = "abacaba"
# k = 4
#
# Output:
# "abac"
#
# Explanation:
# Compare all contiguous substrings of length 4.
# "abac" is lexicographically smallest.
#
# --------------------------------------------------
# Constraints:
#
# 1 <= len(s) <= 1000
# 1 <= k <= len(s)
# s contains lowercase English letters.
#
# Expected:
# Return exactly one substring of length k.


def substring(s,k):
    n=len(s)

    for i in range(n-k+1):
        substring=""
        for j in range(i,i+k):
            substring+=s[j]
        yield substring


def checkSmall(s,k):
    small=""

    for sub in substring(s,k):
        if small=="" or sub<small:
            small=sub
    
    return small

# substring("abcd",3)
print(checkSmall("banana",2))

