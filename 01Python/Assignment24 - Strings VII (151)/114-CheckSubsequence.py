
# Problem: Is Subsequence
# LeetCode 392 - Easy
#
# Description:
# Given two strings s and t, return True if s is a subsequence
# of t, otherwise return False.
#
# A subsequence is a string that can be obtained by deleting
# zero or more characters from another string without changing
# the relative order of the remaining characters.
#
# You cannot rearrange the characters.
#
# Examples:
#
# Test Case 1:
# Input: s = "abc", t = "ahbgdc"
# Output: True
# Explanation: "abc" appears in t in the same order.
#
# Test Case 2:
# Input: s = "axc", t = "ahbgdc"
# Output: False
# Explanation: Character 'x' is not available in t.
#
# Test Case 3:
# Input: s = "", t = "abc"
# Output: True
# Explanation: An empty string is a subsequence of every string.
#
# Test Case 4:
# Input: s = "abc", t = "abc"
# Output: True
# Explanation: Both strings are identical.
#
# Test Case 5:
# Input: s = "ace", t = "abcde"
# Output: True
# Explanation: Characters a, c, e appear in the same order.
#
# Constraints:
# 0 <= len(s) <= 100
# 0 <= len(t) <= 10^4
# s and t consist only of lowercase English letters.
#
# Follow-up:
# Suppose there are lots of incoming s strings and you want
# to check whether each one is a subsequence of t.
# How would you optimize your solution?
#
# Expected Complexity (Two Pointer Approach):
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Where n = length of t.

def approach(s,t):
    i=0
    j=0
    while i<len(s)and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    
    return i==len(s)