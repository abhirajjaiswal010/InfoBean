# Problem: Check if the Sentence Is Pangram
# LeetCode: 1832
#
# A pangram is a sentence where every letter of the English alphabet
# (a-z) appears at least once.
#
# Given a string sentence containing only lowercase English letters,
# return True if sentence is a pangram, otherwise return False.
#
# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: True
#
# Example 2:
# Input: sentence = "leetcode"
# Output: False
#
# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.

# approach-01

def approach01(s):
    unique=set()
    for char in s:
        unique.add(char)
    return len(unique)==26

#approach-02

def approach02(s):
    seen=[False]*26
    for ch in s:
        index=ord(ch)-ord('a')
        seen[index]=True
    return all(seen)
