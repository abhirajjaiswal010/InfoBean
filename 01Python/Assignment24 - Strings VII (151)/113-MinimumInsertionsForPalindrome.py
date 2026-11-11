
# Problem: Minimum Insertions to Make a String Palindrome
#
# Description:
# Given a string s, find the minimum number of characters
# that must be inserted at any position to make the string
# a palindrome.
#
# A palindrome is a string that reads the same forward
# and backward.
#
# You cannot delete or replace existing characters.
# The relative order of original characters must remain unchanged.
#
# Return the minimum number of insertions required.
#
# Examples:
#
# Test Case 1:
# Input:  s = "a"
# Output: 0
# Explanation: A single character is already a palindrome.
#
# Test Case 2:
# Input:  s = "race"
# Output: 3
# Explanation: One possible palindrome is "racecar".
#
# Test Case 3:
# Input:  s = "mbadm"
# Output: 2
# Explanation: Insert 'd' and 'b' to make "mbdadbm".
#
# Test Case 4:
# Input:  s = "leetcode"
# Output: 5
# Explanation: Minimum 5 insertions are required.
#
# Test Case 5:
# Input:  s = "abcda"
# Output: 2
# Explanation: One possible palindrome is "abcdcba".
#
# Constraints:
# 1 <= len(s) <= 1000
# s contains lowercase English letters.
#
# Approach:
# Minimum Insertions = len(s) - LPS(s)
#
# LPS = Longest Palindromic Subsequence
# LPS can be calculated using LCS of the original
# string and its reverse.
#
# Expected Complexity:
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

def approach02(s):
    s1=s
    s2=s[::-1]

    n=len(s1)
    m=len(s2)

    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    return dp[n][m]

s=input("Enter String :")
lps=approach02(s)
print(len(s)-lps)