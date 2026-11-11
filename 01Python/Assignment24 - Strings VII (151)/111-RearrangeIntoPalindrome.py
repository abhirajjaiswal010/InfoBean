# Problem: Check if a String Can Be Rearranged Into a Palindrome
#
# Description:
# Given a string s, determine whether its characters can be
# rearranged to form a palindrome.
#
# A palindrome is a string that reads the same forward and backward.
#
# Return True if the characters can be rearranged to form a palindrome.
# Otherwise, return False.
#
# Examples:
# Input: s = "aabb"
# Output: True
# Explanation: The string can be rearranged as "abba".
#
# Input: s = "abc"
# Output: False
# Explanation: No rearrangement can form a palindrome.
#
# Input: s = "aabbc"
# Output: True
# Explanation: The string can be rearranged as "abcba".
#
# Constraints:
# 1 <= len(s) <= 10^5
# s contains lowercase English letters.


#? my intuition 

# A string can be rearranged into a palindrome
# if the number of characters having odd frequencies
# is less than or equal to 1.

def RearrangePalindrome(s):
    freqCount={}
    odd_count=0

    for ch in s:
        freqCount[ch]=freqCount.get(ch,0)+1

    for freq in freqCount.values():
        # print(freq)
        if freq%2!=0:
            odd_count+=1
    

    # print(odd_count) 
    return odd_count<=1

s=input("Enter : ")
print(RearrangePalindrome(s))
