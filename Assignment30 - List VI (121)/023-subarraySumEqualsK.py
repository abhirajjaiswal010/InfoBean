"""
Question: Subarray Sum Equals K

Given an integer array nums and an integer k, return the total number
of continuous subarrays whose sum equals k.

Test Cases:

1. nums = [1, 1, 1], k = 2
   Output: 2

2. nums = [1, 2, 3], k = 3
   Output: 2

3. nums = [1, -1, 0], k = 0
   Output: 3

4. nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
   Output: 4

5. nums = [1], k = 1
   Output: 1

6. nums = [1], k = 2
   Output: 0

7. nums = [0, 0, 0], k = 0
   Output: 6

8. nums = [1, 2, 1, 2, 1], k = 3
   Output: 4

9. nums = [-1, -1, 1], k = -2
   Output: 2

10. nums = [2, -2, 2, -2], k = 0
    Output: 4
"""


l=list(map(int,input("Enter: ").split()))
k=int(input("Enter K : "))
# count=0
# for i in range(len(l)):
#     sum=0
    
#     for j in range(i,len(l)):
#         # print(l[i:j+1])
#         sum+=l[j]
#         if sum==k:
#             count+=1

# print(count)


prefixSum=0
count=0
freq={0:1}


for n in l:
    prefixSum+=n

    required=prefixSum-k

    if required in freq:
        count+=freq[required]
    
    freq[prefixSum]=freq.get(prefixSum,0)+1

print(count)

