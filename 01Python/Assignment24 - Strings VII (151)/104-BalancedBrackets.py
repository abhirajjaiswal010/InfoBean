
# Problem: Balanced Brackets (Valid Parentheses)
#
# Given a string s containing the following brackets:
# '(', ')', '{', '}', '[' and ']'.
#
# Determine whether the brackets in the string are balanced.
#
# A string is considered balanced if:
# 1. Every opening bracket has a corresponding closing bracket.
# 2. Every opening bracket is closed by the same type of bracket.
# 3. Brackets are closed in the correct order.
#
# Return True if the brackets are balanced; otherwise, return False.
#
# Examples:
#
# Input: s = "{[()]}"
# Output: True
# Explanation: All brackets are properly matched and nested.
#
# Input: s = "([)]"
# Output: False
# Explanation: Brackets are not closed in the correct order.
#
# Input: s = "()[]{}"
# Output: True
# Explanation: All brackets are correctly balanced.
#
# Input: s = "((("
# Output: False
# Explanation: Opening brackets are not closed.
#
# Input: s = ")))"
# Output: False
# Explanation: Closing brackets have no matching opening brackets.
#
# Constraints:
# 1 <= len(s) <= 10^4
# s consists of brackets only: (){}[]


def stackApproach2(s):
     stack=[]
     for ch in s:
          if ch=='(':
               stack.append(')')
          elif ch=='{':
               stack.append('}')
          elif ch=='[':
               stack.append(']')
          else:
               if not stack or stack.pop!=ch:
                    return False
     return len(stack)==0

s=input("Enter :")
print(stackApproach2(s))