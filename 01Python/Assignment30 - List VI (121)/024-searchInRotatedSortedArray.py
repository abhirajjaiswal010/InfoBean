'''
Search in Rotated Sorted Array -> binary search 

Question:

You are given a sorted array of integers that has been rotated at
an unknown position.

Your task is to find the index of a given target element in the
rotated array.

The array was originally sorted in ascending order, but after
rotation, the elements may appear in two sorted parts.

For example:

Original array:
#*   [0, 1, 2, 4, 5, 6, 7]

After rotation:
#&   [4, 5, 6, 7, 0, 1, 2]

Here, the array is still partially sorted, but the smallest
elements have been moved to the beginning/end because of rotation.

#& If the target exists in the array, return its index.

#& If the target does not exist, return -1.

Requirement:
Solve the problem using Binary Search with O(log n) time complexity.

Test Case 1:
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

Expected Output:
4

Explanation:
The target 0 is present at index 4.

Test Case 2:
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

Expected Output:
-1

Explanation:
The target 3 does not exist in the array.

Test Case 3:
Input:
nums = [6, 7, 8, 1, 2, 3, 4, 5]
target = 3

Expected Output:
5

Explanation:
The target 3 is present at index 5.

Test Case 4:
Input:
nums = [5, 6, 7, 8, 1, 2, 3, 4]
target = 8

Expected Output:
3

Explanation:
The target 8 is present at index 3.

Test Case 5:
Input:
nums = [1]
target = 1

Expected Output:
0

Explanation:
The array contains only one element, and that element is the target.
'''



