'''
Docstring for Assignment22 - String V.a04
Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''

# n=input("Enter : ")

# count=0
# e=""

# for i in n:
    
#     temp=0

#     for j in n:
#         if i==j:
#             temp+=1
        
#     if temp>count:
#         count=temp
        

# print(count)

# for i  in n:
#     temp=0
#     for j in n:
#         if i==j:
#             temp+=1
    
#     if temp==count and i not in e :
#         e+=i+" "

# print(e)


#dictionary

n = input("Enter : ")

freq = {}

for i in n:

    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

high = 0 # -> 3


for i in freq:

    if freq[i] > high:
        high = freq[i]
        

print(high)


wo=""
for i in freq:
    if freq[i]==high:
        wo+=i+" "

print(wo)