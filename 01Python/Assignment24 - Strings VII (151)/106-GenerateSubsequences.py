# Problem: Generate All Subsequences of a String
#
# Given a string s, generate all possible subsequences
# of the string while maintaining the relative order
# of characters.
#
# A subsequence is a sequence that can be obtained by
# deleting zero or more characters without changing
# the order of the remaining characters.
#
# Input:
# s = "abc"
#
# Output:
# a
# b
# c
# ab
# ac
# bc
# abc
#
# Note:
# The empty subsequence "" is also valid.
#
# Total number of subsequences = 2^n
#
# Constraints:
# 1 <= len(s) <= 20



def bruteForce(s):

    n=len(s)
    for i in range(n+1):
        for j in range(i,n+1):
            for k in range(j,n+1):
                current=s[i:j]+s[j:k]
                print(current)



def generateSubsquence(s,index,current):
    if index==len(s):
        if not current:
            print("empty")
        else:
            print(current)
        return
    
    generateSubsquence(s,index+1,current+s[index])
    generateSubsquence(s,index+1,current)

# s="abc"
# generateSubsquence(s,0,"")


def countSubsequence(s,index):
    if index==len(s):
        return 1
    
    pick=countSubsequence(s,index+1)
    notPick=countSubsequence(s,index+1)
    return pick+notPick
s=input("Enter The String : ")
print(f"count of {s} : {countSubsequence(s,0)}")


def sumCheck(s,index,current,target):

    if index==len(s):
        if current==target:
            return 1
        return 0
    
    pick=sumCheck(s,index+1,current+s[index],target)
    notpick=sumCheck(s,index+1,current,target)

    return pick+notpick



        