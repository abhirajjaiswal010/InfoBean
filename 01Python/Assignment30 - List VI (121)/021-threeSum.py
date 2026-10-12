'''
Given an integer array nums, find all unique triplets
[a, b, c] such that:

    a + b + c = 0

Return all the triplets in the array.

Each triplet must contain three different indices,
and the solution must not contain duplicate triplets.

Example:

Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2],
 [-1, 0, 1]]

Explanation:
- (-1) + (-1) + 2 = 0
- (-1) + 0 + 1 = 0

The order of the triplets does not matter.
'''



l=[-1,0,1,2,-1,-4]
l.sort()
# print(l)
ans=[]
for i in range(len(l)):

    n1=l[i]  #fixed
    target=-n1
    # print(target)
    #& check duplicate for fixed or n1
    if i>0 and l[i] == l[i - 1]:
        continue

    left=i+1
    right=len(l)-1
    ansSub=[]

    while(left<right):
        sum=l[left]+l[right]
            

        if sum==target:
            ansSub=[n1,l[left],l[right]]
            ans.append(ansSub)
            left+=1
            right-=1

            while  left<right and l[left]==l[left-1]:
                left+=1

            while left <right and l[right]==l[right+1]:
                right-=1


        elif sum<target:
            left+=1
        else:
            right-=1
    
    

print(ans)

    






    