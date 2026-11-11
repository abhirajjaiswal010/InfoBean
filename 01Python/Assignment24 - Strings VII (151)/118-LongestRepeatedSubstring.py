
# Problem: Find the Longest Repeated Substring
#
# Given a string s, find the longest substring that appears
# at least twice in the given string.
#
# A substring is a contiguous sequence of characters within a string.
#
# The repeated occurrences may overlap with each other.
#
# Return the longest repeated substring.
# If no repeated substring exists, return an empty string "".
#
# Example 1:
# Input: s = "banana"
# Output: "ana"
# Explanation:
# The substring "ana" appears twice in "banana".
#
# Example 2:
# Input: s = "abcd"
# Output: ""
# Explanation:
# No substring is repeated.
#
# Example 3:
# Input: s = "aaaa"
# Output: "aaa"
# Explanation:
# The substring "aaa" appears twice (overlapping occurrences).
#
# Example 4:
# Input: s = "abcabc"
# Output: "abc"
# Explanation:
# The substring "abc" appears twice.
#
# Example 5:
# Input: s = "ababab"
# Output: "abab"
# Explanation:
# The substring "abab" appears twice (overlapping occurrences).
#
# Example 6:
# Input: s = "mississippi"
# Output: "issi"
# Explanation:
# The substring "issi" appears twice.
#
# Constraints:
# 1 <= len(s) <= 1000
# s consists of lowercase English letters.
#
# Follow-up:
# Can you solve this problem more efficiently than O(n^3)?

def bruteForce(s):
    n=len(s)
    ans=""
    seen=[]

    for i in range(n):
        temp=""
        for j in range(i,n):
            temp+=s[j]
            # print(temp)
            if temp in seen:
                if len(temp)>len(ans):
                    ans=temp
            else:
                seen.append(temp)
    
    return ans

print(bruteForce("banana"))
