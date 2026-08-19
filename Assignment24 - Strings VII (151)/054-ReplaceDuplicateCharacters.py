'''
Question:
Replace all duplicate characters with '$'.

Given a string, identify all characters that occur
more than once. Replace every occurrence of those
duplicate characters with '$'.

Characters that occur only once should remain unchanged.

Test Cases:

1. Input:
   hello
   Output:
   he$$o

2. Input:
   banana
   Output:
   b$$$$$

3. Input:
   programming
   Output:
   $rog$am$$n$

4. Input:
   abcde
   Output:
   abcde

5. Input:
   aabbcc
   Output:
   $$$$$$

6. Input:
   apple
   Output:
   a$$le

7. Input:
   success
   Output:
   $u$$$$

8. Input:
   112233
   Output:
   $$$$$$

9. Input:
   python
   Output:
   python

10. Input:
    mississippi
    Output:
    m$$$$$$$$$$
'''

s=input("Enter The String : ")
new=""

for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    
    if count!=1:
        new+="$"

    else:
        new+=i

print(new)

