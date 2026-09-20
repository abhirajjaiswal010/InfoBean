'''
Missing Number

Given an array nums containing n distinct numbers taken from the range [0, n],
find the one missing number from the array.

Return the missing number.

Example 1:
Input:
nums = [3, 0, 1]

Output:
2

Explanation:
The numbers from 0 to 3 are [0, 1, 2, 3].
The number 2 is missing.

Example 2:
Input:
nums = [0, 1]

Output:
2

Example 3:
Input:
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

Output:
8

Constraints:
1 <= len(nums) <= 10^4
0 <= nums[i] <= n
All numbers are distinct.
Exactly one number is missing.
'''

l=list(map(int,input("Enter : ").split()))


n=len(l)
missing=n
for i in range(n):
    missing=missing^i^l[i]

print(missing)
