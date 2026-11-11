# Problem: Largest Lexicographical Substring
#
# Given a string s, find the lexicographically largest substring
# of the given string.
#
# A substring is a contiguous sequence of characters within a string.
#
# Lexicographically larger means the substring that comes later
# in dictionary order when compared with other substrings.
#
# Return the lexicographically largest substring.
#
# Example 1:
# Input: s = "abab"
# Output: "bab"
#
# Explanation:
# All possible substrings include:
# "a", "ab", "aba", "abab", "b", "ba", "bab"
#
# The lexicographically largest substring is "bab".
#
# Example 2:
# Input: s = "leetcode"
# Output: "tcode"
#
# Constraints:
# 1 <= len(s) <= 10^5
# s contains only lowercase English letters.


def substring(s):
    n=len(s)

    for i in range(n):
        substring=""
        for j in range(i,n):
            substring+=s[j]
        yield substring


def checkLarge(s):
    large=""

    for sub in substring(s):
        if large=="" or sub>large:
            large=sub
    
    return large

# substring("abcd",3)
print(checkLarge("abab"))