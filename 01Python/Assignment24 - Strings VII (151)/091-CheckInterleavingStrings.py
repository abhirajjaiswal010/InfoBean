# Check if Two Strings Are a Valid Interleaving of a Third String
# Problem Description:

# You are given three strings s1, s2, and s3. Your task is to determine whether s3 can be formed by interleaving the characters of s1 and s2.

# A string s3 is considered a valid interleaving if:
# 1. All characters of s1 and s2 are used exactly once.
# 2. The relative order of characters from each original string must be preserved.
# 3. Characters from s1 and s2 can be mixed in any order, but their individual sequences cannot be rearranged.
# Return True if s3 is a valid interleaving of s1 and s2; otherwise, return False.

# Example Test Cases:

# Test Case 1:
# s1 = "abc"s2 = "def"s3 = "adbcef"Output: True



# Explanation: Characters are picked in this order:
# - a from s1
# - d from s2
# - b from s1
# - c from s1
# - e from s2
# - f from s2
# Both original character sequences remain in their correct order.

# Test Case 2:
# s1 = "aabcc"s2 = "dbbca"s3 = "aadbbcbcac"Output: True



# Explanation: The characters of s3 can be divided into two subsequences:
# - From s1: a → a → b → c → c
# - From s2: d → b → b → c → a
# Both subsequences preserve their original order.

# Test Case 3:
# s1 = "aabcc"s2 = "dbbca"s3 = "aadbbbaccc"Output: False



# Explanation: Although the characters may appear similar, it is impossible to select characters from both strings while preserving the original order and forming s3.

# Test Case 4:
# s1 = "abcde"s2 = "xyz"s3 = "axbyczde"Output: True



# Explanation: Characters are alternately selected from both strings. The complete sequence of s1 and s2 is maintained.

# Test Case 5:
# s1 = "abc"s2 = "defg"s3 = "adbecfg"Output: False



# Explanation: The combined length is correct, but the character ordering does not allow s3 to be formed by interleaving s1 and s2.

# Constraints:
# - \(0 \leq len(s1), len(s2) \leq 100\)
# - \(0 \leq len(s3) \leq 200\)
# - s1, s2, and s3 contain lowercase English letters.
# - The length of s3 must equal len(s1) + len(s2).


#? two pinter se mein ambiguity face kar rha hu 

#? because mere pass choice hai toh mujhe recursion try karna chaiye 


def recursionApproach(s1,s2,s3):

    if len(s1)+len(s2)!=len(s3):
        return False
    
    def solve(i,j,k):
        if k==len(s3):
            return True
        
        if i<len(s1) and s1[i]==s3[k]:
            if solve(i+1,j,k+1):
                return True
        
        if j<len(s2) and s2[j]==s3[k]:
            if solve(i,j+1,k+1):
                return True
        return False
    
    return solve(0,0,0)

s1=input("Enter s1 :")
s2=input("Enter s2 :")
s3=input("Enter s3 :")

print(recursionApproach(s1,s2,s3))


def recursionMemoApproach(s1,s2,s3):



    if len(s1)+len(s2)!=len(s3):
        return False
    
    m=len(s1)
    n=len(s2)
    l=len(s3)

    dp=[[[0 for k in range(l+1)]
         for j in range(n+1)]
         for i in range(m+1)]
    
    def solve(i,j,k,dp):
        if k==len(s3):
            return True
        
        if dp[i][j][k]!=0:
            return dp[i][j][k]==1
        
        if i<len(s1) and s1[i]==s3[k]:
            if solve(i+1,j,k+1,dp):
                dp[i][j][k]=1
                return True
        
        if j<len(s2) and s2[j]==s3[k]:
            if solve(i,j+1,k+1,dp):
                dp[i][j][k]=1
                return True
        
        dp[i][j][k]=-1
        return False
    
    return solve(0,0,0,dp)


def recursionMemo2DApproach(s1,s2,s3):



    if len(s1)+len(s2)!=len(s3):
        return False
    
    m=len(s1)
    n=len(s2)
   

    dp=[[
         0 for j in range(n+1)]
         for i in range(m+1)]
    
    def solve(i,j,dp):
        if i+j==len(s3):
            return True
        
        if dp[i][j]!=0:
            return dp[i][j]==1
        
        if i<len(s1) and s1[i]==s3[i+j]:
            if solve(i+1,j,dp):
                dp[i][j]=1
                return True
        
        if j<len(s2) and s2[j]==s3[i+j]:
            if solve(i,j+1,dp):
                dp[i][j]=1
                return True
        
        dp[i][j]=-1
        return False
    
    return solve(0,0,dp)


    
        

    

    


