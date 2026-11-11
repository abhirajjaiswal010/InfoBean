
# Problem: Find the Longest Substring Containing Only Vowels
#
# Given a string s, find the length of the longest contiguous
# substring that contains only English vowels:
# 'a', 'e', 'i', 'o', 'u'.
#
# A substring must contain consecutive characters from the string.
#
# Return the length of the longest valid substring.
#
# If no vowel exists, return 0.
#
# Example 1:
# Input: s = "aeiou"
# Output: 5
# Explanation: The entire string contains only vowels.
#
# Example 2:
# Input: s = "hello"
# Output: 1
# Explanation: The longest valid substrings are "e" and "o".
#
# Example 3:
# Input: s = "aaaeee"
# Output: 6
# Explanation: The entire string contains only vowels.
#
# Example 4:
# Input: s = "abcdeiouxyz"
# Output: 4
# Explanation: The longest valid substring is "eiou".
#
# Example 5:
# Input: s = "xyz"
# Output: 0
# Explanation: No vowels are present.
#
# Example 6:
# Input: s = "aabeioouu"
# Output: 9
# Explanation: The entire string contains only vowels.
#
# Example 7:
# Input: s = "xxaeiouyy"
# Output: 5
# Explanation: The longest valid substring is "aeiou".
#
# Constraints:
# 1 <= len(s) <= 10^5
# s contains lowercase English letters.
#
# Follow-up:
# Can you solve this problem using Sliding Window
# in O(n) time complexity?
#
# DSA Pattern:
# Variable Size Sliding Window

def longestVowel(s):
    vowel="aeiou"
    left=0
    ans=0

    for right in range(len(s)):
        if s[right] not in vowel:
            left=right+1
        else:
            ans=max(ans,right-left+1)

    return ans 


print(longestVowel("aeiou"))       # 5
print(longestVowel("hello"))       # 1
print(longestVowel("aaaeee"))      # 6
print(longestVowel("xyz"))         # 0
print(longestVowel("xxaeiouyy"))   # 5

# Algorithm 
# 1. right se string traverse karo.
# 2. Agar vowel mile, current window ki length calculate karo.
# 3. Agar consonant mile, left = right + 1 kar do.
# 4. Har step par maximum length update karo.