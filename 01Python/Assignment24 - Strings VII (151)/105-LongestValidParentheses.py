
# Problem: Longest Valid Parentheses
#
# Given a string s containing only '(' and ')',
# find the length of the longest valid (well-formed)
# parentheses substring.
#
# A valid parentheses substring must satisfy:
# 1. Every opening parenthesis has a matching closing parenthesis.
# 2. Parentheses must be closed in the correct order.
#
# Return the length of the longest valid parentheses substring.
#
# Examples:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid substring is "()".
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid substring is "()()".
#
# Input: s = ""
# Output: 0
# Explanation: The string is empty.
#
# Input: s = "((()))"
# Output: 6
# Explanation: The entire string is valid.
#
# Input: s = "()(()"
# Output: 2
# Explanation: The longest valid substring is "()".
#
# Input: s = "()(())"
# Output: 6
# Explanation: The entire string is valid.
#
# Constraints:
# 0 <= len(s) <= 3 * 10^4
# s[i] is '(' or ')'.
#
# Follow-up:
# Can you solve this problem using:
# 1. Brute Force
# 2. Dynamic Programming
# 3. Stack
# 4. Two Traversals (Counter approach)

def longValid1(s):

    stack=[-1]
    long_len=0

    for i in range(len(s)):
        if s[i]=="(":
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                long_len=max(long_len,i-stack[-1])
    return long_len
        

# s=input("Enter :")
# print(longValid1(s))


# Algorithm:
#
# 1. Ek empty stack banane ke bajaye [-1] initialize karo.
#    -1 ek initial boundary index represent karta hai.
#
# 2. Ek long_len variable banao jo maximum valid
#    parentheses substring ki length store karega.
#
# 3. String ko left se right traverse karo.
#
# 4. Agar current character "(" hai:
#       - Uska index stack mein push karo.
#
# 5. Agar current character ")" hai:
#       - Stack se top index pop karo.
#
#       - Agar stack empty ho jaye:
#           Current index ko stack mein push karo.
#           Kyunki unmatched closing bracket ek new boundary
#           create karta hai.
#
#       - Otherwise:
#           Current valid substring ki length calculate karo:
#           current_index - stack[-1]
#
#           long_len ko maximum length se update karo.
#
# 6. Traversal complete hone ke baad long_len return karo.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def longValid2(s):
    open_count=0
    close_count=0
    long_len=0

    for ch in s:

        if ch=="(":
            open_count+=1
        else:
            close_count+=1
        
        if open_count==close_count:
            long_len=max(long_len,2*close_count)
        
        elif close_count>open_count:
            open_count=0
            close_count=0
    
   
    open_count=0
    close_count=0
    for ch in reversed(s):

        if ch=="(":
            open_count+=1
        else:
            close_count+=1
        
        if open_count==close_count:
            long_len=max(long_len,2*open_count)
        
        elif close_count<open_count:
            open_count=0
            close_count=0
    
    return long_len




     
