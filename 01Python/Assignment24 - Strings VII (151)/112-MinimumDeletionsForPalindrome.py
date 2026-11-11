# Problem: Minimum Deletions to Make a String Palindrome
#
# Description:
# Given a string s, find the minimum number of characters
# that need to be deleted to make the string a palindrome.
#
# You can delete any character from the string.
# The remaining characters must maintain their original relative order.
#
# Return the minimum number of deletions required.
#
# Examples:
#
# Example 1:
# Input: s = "aebcbda"
# Output: 2
# Explanation:
# Delete 'e' and 'd' to get "abcba", which is a palindrome.
#
# Example 2:
# Input: s = "aba"
# Output: 0
# Explanation:
# The string is already a palindrome.
#
# Example 3:
# Input: s = "abc"
# Output: 2
# Explanation:
# Delete 'b' and 'c' to get "a", which is a palindrome.
#
# Constraints:
# 1 <= len(s) <= 1000
# s contains lowercase English letters.
#
# Follow-up:
# Can you solve this problem using Dynamic Programming?


def approach01(s,left,right):
    if left>=right:
        return 0
    
    if s[left]==s[right]:
        return approach01(s,left+1,right-1)
    
    else:
        left_result=approach01(s,left+1,right)
        right_result=approach01(s,left,right-1)
    
    return 1+min(left_result,right_result)


# s=input("Enter :")

# print(approach01(s,0,len(s)-1))


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
            
