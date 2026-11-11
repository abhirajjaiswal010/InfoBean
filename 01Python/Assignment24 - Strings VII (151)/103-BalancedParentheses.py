"""
Problem: Balanced Parentheses

Description:

Given a string containing opening and closing parentheses,
determine whether the parentheses are balanced.

A string is considered balanced if:

1. Every opening parenthesis '(' has a corresponding
   closing parenthesis ')'.

2. Every opening parenthesis must be closed.

3. Parentheses must be closed in the correct order.

Examples:

Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "(())"
Output: True

Example 3:
Input: s = "()()"
Output: True

Example 4:
Input: s = "(()"
Output: False

Example 5:
Input: s = "())"
Output: False

Example 6:
Input: s = "((()))"
Output: True

Example 7:
Input: s = "))(("
Output: False

Constraints:
1 <= len(s) <= 10^4
s contains only '(' and ')' characters.

Follow-up:
1. Solve using a counter.
2. Solve using a stack.
3. Solve using recursion.

Expected Complexity:
Time Complexity: O(n)
Space Complexity:
- Counter approach: O(1)
- Stack approach: O(n)
"""


def counterApproach(s):
   count = 0
   valid = True

   for ch in s:
      if ch == "(":
            count += 1
      elif ch == ")":
            count -= 1
      if count < 0:
            valid = False
            break
   if count!=0:
        valid=False
   return valid

# s=input("Enter String : ")
# print(counterApproach(s))

#! 1. Logic – Stack Approach
# Stack follows LIFO (Last In, First Out).
# 1. If the character is an opening bracket, push it into the stack.
# 2. If the character is a closing bracket:
#    - Check whether the stack is empty.
#    - Pop the top opening bracket.
#    - Check whether it matches the closing bracket.
# 3. At the end, the stack must be empty.

def stackApproach(s):
     stack=[]
     for ch in s:
          
          if ch=="(" or ch=="{" or ch=="[" :
               stack.append(ch)
          else:
               if not stack:
                    return False
               top=stack.pop()

               if ch==")" and top!="(":
                    return False
               elif ch=="}" and top!="{":
                    return False
               elif ch==']' and top!='[':
                    return False
               
     return len(stack)==0
      
# s=input("Enter :")
# print(stackApproach(s))


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