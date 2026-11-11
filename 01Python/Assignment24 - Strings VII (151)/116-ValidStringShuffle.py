# # Problem: Valid String Shuffle

# # You are given three strings: s1, s2, and result.
# # Determine whether result is a valid shuffle of s1 and s2.

# # A valid shuffle must satisfy:
# # 1. All characters of s1 and s2 must be present in result.
# # 2. The relative order of characters in s1 must remain unchanged.
# # 3. The relative order of characters in s2 must remain unchanged.
# # 4. Characters from both strings can be interleaved in any order.

# # Return True if result is a valid shuffle; otherwise, return False.


# # Test Case 1: Easy
# s1 = "abc"
# s2 = "def"
# result = "adbcef"
# # Output: True


# # Test Case 2: Easy
# s1 = "abc"
# s2 = "xyz"
# result = "axbycz"
# # Output: True


# # Test Case 3: Medium
# s1 = "abc"
# s2 = "def"
# result = "abdfec"
# # Output: False


# # Test Case 4: Medium
# s1 = "aab"
# s2 = "axy"
# result = "aaxaby"
# # Output: True


# # Test Case 5: Hard
# s1 = "aabc"
# s2 = "abad"
# result = "aababadc"
# # Output: True


# # Constraints:
# # 1 <= len(s1), len(s2) <= 10^5
# # len(s1) + len(s2) == len(result)
# # All strings contain lowercase English letters.


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

result=recursionApproach(s1,s2,s3)

if result:
    print("valid")
else:
    print("invalid")