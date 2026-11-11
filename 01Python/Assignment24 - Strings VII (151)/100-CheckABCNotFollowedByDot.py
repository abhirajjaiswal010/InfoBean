# Problem: Check Whether "abc" Is Not Followed by a Dot (.)

# Description:
# Given a string, check whether the substring "abc" is immediately
# followed by a dot (.) or not.
#
# Return True if "abc" is not followed by a dot.
# Return False if "abc" is immediately followed by a dot.
#
# Examples:
# Input:  "helloabc"
# Output: True
#
# Input:  "helloabc.xyz"
# Output: False
#
# Input:  "abc123"
# Output: True
#
# Input:  "abctest.abc"
# Output: True
#
# Input:  "abc."
# Output: False
#
# Constraints:
# - The string may contain lowercase letters, uppercase letters,
#   digits, and special characters.
# - The substring "abc" may occur multiple times.with


def checkString(s):
    for i in range(len(s)-2):

        if (s[i]=="a" and s[i+1]=="b" and s[i+2]=="c"):
            if i+3<len(s) and s[i+3]==".":
                return False

    return True

print(checkString("helloabc"))
print(checkString("helloabc.xyz"))
    
