
# Problem: Edit Distance
# LeetCode 72 - Medium
#
# Description:
# Given two strings word1 and word2, return the minimum
# number of operations required to convert word1 into word2.
#
# You are allowed to perform the following three operations:
#
# 1. Insert:
#    Insert any character at any position in word1.
#
# 2. Delete:
#    Remove any character from word1.
#
# 3. Replace:
#    Replace any character in word1 with another character.
#
# Each operation has a cost of 1.
#
# Return the minimum number of operations required
# to convert word1 into word2.
#
# Examples:
#
# Test Case 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse  (Replace 'h' with 'r')
# rorse -> rose   (Delete 'r')
# rose  -> ros    (Delete 'e')
#
# Test Case 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# Five operations are required to convert
# "intention" into "execution".
#
# Test Case 3:
# Input: word1 = "", word2 = "abc"
# Output: 3
# Explanation:
# Insert 'a', 'b', and 'c'.
#
# Test Case 4:
# Input: word1 = "abc", word2 = ""
# Output: 3
# Explanation:
# Delete all three characters.
#
# Test Case 5:
# Input: word1 = "abc", word2 = "abc"
# Output: 0
# Explanation:
# Both strings are already identical.
#
# Constraints:
# 0 <= word1.length <= 500
# 0 <= word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
# Follow-up:
# Can you solve this problem using:
# 1. Recursion (Brute Force)
# 2. Recursion + Memoization
# 3. Dynamic Programming (Tabulation)
# 4. Space-Optimized Dynamic Programming
#
# Expected Complexity:
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
#
# Hint:
# If word1[i] == word2[j]:
#     No operation is required.
#
# Otherwise, consider:
#     Insert  -> 1 + dp[i][j-1]
#     Delete  -> 1 + dp[i-1][j]
#     Replace -> 1 + dp[i-1][j-1]
#
# Take the minimum of all three operations.

def approach01(s1,s2):
        m = len(s1)
        n = len(s2)

        dp = [[-1] * n for _ in range(m)]

        

        def solve(s1, s2, i, j, dp):

            if i < 0:
                return j + 1

            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = solve(s1, s2, i - 1, j - 1, dp)
                return dp[i][j]

            insert = solve(s1, s2, i, j - 1, dp)
            delete = solve(s1, s2, i - 1, j, dp)
            replace = solve(s1, s2, i - 1, j - 1, dp)

            dp[i][j] = 1 + min(insert, delete, replace)

            return dp[i][j]
        
        return solve(s1,s2,m-1,n-1,dp)