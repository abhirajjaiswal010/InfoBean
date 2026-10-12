'''
Docstring for Assignment18.a02
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''

n=input("Enter : ").strip()
count=0
i=0
while i <len(n):
    if n[i]==" ":
        count+=1
    i+=1


print(count)


n = input("Enter: ")

count = 0
i = 0

while i < len(n):
    if n[i] == " ":
        if i != 0 and i != len(n) - 1:
            # Agar current character space hai AND woh first ya last character nahi hai, tab count karo.
            count += 1
    i += 1

print("Total spaces:", count)