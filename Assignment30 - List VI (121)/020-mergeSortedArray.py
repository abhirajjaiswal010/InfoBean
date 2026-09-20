'''
Merge Sorted Array

You are given two sorted integer arrays nums1 and nums2.
Merge nums2 into nums1 so that nums1 becomes sorted in
ascending order.

nums1 has a size of m + n, where:
- The first m elements contain valid values.
- The last n elements are 0 placeholders.

nums2 contains n sorted elements.

Modify nums1 in-place.

Example 1:

Input:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Output:
[1, 2, 2, 3, 5, 6]

Example 2:

Input:
nums1 = [1]
m = 1
nums2 = []
n = 0

Output:
[1]

Example 3:

Input:
nums1 = [0]
m = 0
nums2 = [1]
n = 1

Output:
[1]

Constraints:
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 are sorted in non-decreasing order.
'''


nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:

    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1

    k -= 1

while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(nums1)