"""
LeetCode 125: Valid Palindrome

Problem Statement:

A phrase is considered a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward.

Alphanumeric characters include letters (A-Z, a-z) and numbers (0-9).

Given a string s, return True if it is a palindrome, or False otherwise.

Examples:

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: True
Explanation: After removing non-alphanumeric characters,
             the string becomes empty, which is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

Follow-up:
Can you solve it using O(1) extra space?
"""


# ? approach - 01
def validPalindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalnum():
            left += 1

        elif not s[right].isalnum():
            right -= 1

        elif s[left].lower() != s[right].lower():
            return False

        else:
            left += 1
            right -= 1

    return True


# ? approach - 02


def validPalindDrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if not (
            ("a" <= s[left] <= "z") or "A" <= s[left] <= "Z" or "0" <= s[left] <= "9"
        ):
            left += 1
            continue
        if not (
            ("a" <= s[right] <= "z") or "A" <= s[right] <= "Z" or "0" <= s[right] <= "9"
        ):
            right -= 1
            continue
        
        l=s[left]
        r=s[right]

        if 'A'<=l<='Z':
            l=chr(ord(l)+32)
        
        if 'A'<=r<='Z':
            r=chr(ord(r)+32)
        
        if l!=r:
            return False
        
        left+=1
        right-=1
    
    return True

print(validPalindDrome2("A man, a plan, a canal: Panama"))