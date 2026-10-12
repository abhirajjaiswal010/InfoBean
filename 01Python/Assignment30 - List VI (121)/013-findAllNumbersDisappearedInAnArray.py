'''
Problem 13: Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range
[1, n], return all the integers in the range [1, n] that do not
appear in nums.

Example 1:
Input:
nums = [4, 3, 2, 7, 8, 2, 3, 1]

Output:
[5, 6]

Explanation:
The numbers from 1 to 8 are:
[1, 2, 3, 4, 5, 6, 7, 8]

Numbers 5 and 6 do not appear in the array.

Example 2:
Input:
nums = [1, 1]

Output:
[2]

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
'''

l=list(map(int,input("Enter : ").split()))


for i in l:
    index=abs(i)-1
    l[index]=-abs(l[index])

print(l)
ans=[]
for i in range(len(l)):
    if l[i]>0:
        ans.append(i+1)

print(ans)
        


'''
Algorithm
1.Array ke har num ko traverse karo.

2.num ka corresponding index nikalo:

3.index = abs(num) - 1
4.Us index ke element ko negative mark karo.
5.Pura array traverse karne ke baad:
6.Agar nums[i] > 0 hai → i + 1 missing hai.
7.Agar nums[i] < 0 hai → i + 1 present hai.
8.Saare positive positions ke corresponding numbers ko answer mein add karo.

'''