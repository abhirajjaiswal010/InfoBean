
# Problem: Check if a String Contains Duplicate Substrings
#
# You are given a string s and an integer k.
# Your task is to determine whether the string contains
# any duplicate substring of length exactly k.
#
# A substring is a contiguous sequence of characters
# within a string.
#
# Two substrings are considered duplicates if:
# 1. They contain exactly the same characters.
# 2. They appear at different starting positions.
# 3. Their length is exactly k.
#
# Return True if at least one duplicate substring exists;
# otherwise, return False.
#
# Example 1:
# Input:  s = "abcabc", k = 3
# Output: True
# Explanation: "abc" appears at indices 0 and 3.
#
# Example 2:
# Input:  s = "abcdef", k = 2
# Output: False
# Explanation: All substrings of length 2 are unique.
#
# Example 3:
# Input:  s = "banana", k = 2
# Output: True
# Explanation: "an" appears at multiple positions.
#
# Example 4:
# Input:  s = "aaaaa", k = 2
# Output: True
# Explanation: "aa" appears at multiple positions.
#
# Example 5:
# Input:  s = "abacabad", k = 3
# Output: True
# Explanation: "aba" appears at indices 0 and 4.
#
# Constraints:
# 1 <= len(s) <= 10^5
# 1 <= k <= len(s)
# s contains lowercase English letters.

def bruteForce(s,k):
    seen=[]

    for i in range(len(s)):
        temp=""
        for j in range(i,len(s)):
            temp+=s[j]
        
            if len(temp)==k:
                if temp in seen:
                    return True
                seen.append(temp)
                # print(temp)
                break
    return False

# s=input("Enter :")
# k=int(input("Enter K :"))
# print(bruteForce(s,k))
        
def slidingAppoarch(s,k):
    seen=set()

    for i in range(len(s)-k+1):
        # temp=s[i:i+k]
        temp=""
        for j in range(i,i+k):
            temp+=s[j]


        if temp in seen:
            return True
        
        seen.add(temp)

    return False

s=input("Enter :")
k=int(input("Enter K :"))
print(slidingAppoarch(s,k))

