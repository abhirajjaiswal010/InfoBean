"""
Problem: Reverse a String Using Recursion

Description:
Given a string s, write a recursive function to reverse the
string without using built-in reverse methods or slicing.

Your task is to return the reversed string.

Examples:

Example 1:
Input: s = "hello"
Output: "olleh"

Example 2:
Input: s = "Python"
Output: "nohtyP"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "abcd"
Output: "dcba"

Constraints:
1 <= len(s) <= 10^5
s contains printable characters.

Follow-up:
1. Solve the problem using recursion.
2. Solve without using string slicing.
3. Try solving using an index parameter.

Expected Complexity:
Time Complexity: O(n) or O(n^2), depending on approach.
Space Complexity: O(n) for the recursion stack.
"""

def reverseString(s,left,right):
   if left>=right:
      return s
   
   s[left],s[right]=s[right],s[left]

   return reverseString(s,left+1,right-1)

# s=list(input("Enter The string : "))
# result=reverseString(s,0,len(s)-1)
# print("".join(result))


def reverseStringIndex(s,index):
   if index<0:
      return ""
   
   return s[index]+reverseStringIndex(s,index-1)

s="hello"
print(reverseStringIndex(s,len(s)-1))

