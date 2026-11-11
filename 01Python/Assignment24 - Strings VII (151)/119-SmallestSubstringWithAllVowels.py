
# Problem: Find the Smallest Substring Containing All Vowels
#
# Given a string s, find the smallest contiguous substring
# that contains all five English vowels:
# 'a', 'e', 'i', 'o', 'u' at least once.
#
# Return the length of the smallest valid substring.
#
# If no such substring exists, return -1.
#

# # Test Case 1
# s = "aeiou"
# # Output: 5

# # Test Case 2
# s = "abcdeiouxyz"
# # Output: 5

# # Test Case 3
# s = "aaeeiioouu"
# # Output: 9

# # Test Case 4
# s = "leetcode"
# # Output: -1

# # Test Case 5
# s = "abecidofu"
# # Output: 9

# # Test Case 6
# s = "xyzuaeiopqr"
# # Output: 5
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


def smallestSubstring(s):
    vowels = set("aeiou")
    freq = {}

    left = 0
    ans = float('inf')

    for right in range(len(s)):

        if s[right] in vowels:
            freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) == 5:

            ans = min(ans, right - left + 1)

            if s[left] in vowels:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

            left += 1

    return ans if ans != float('inf') else -1

print(smallestSubstring("abcdeiouxyz"))