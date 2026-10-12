# 10. Trim leading, trailing, or extra spaces from a string.


# s=input("Enter The String : ")
# print(" ".join(s.split()))


#method - 2

s = input("Enter The String : ")

new = ""
space = False

for i in s:

    if i != " ":
        new += i
        space = False

    elif not space:
        new += i #only one space
        
        space = True

# Leading and trailing spaces remove karo
if new != "":
    if new[0] == " ":
        new = new[1:]

    if new[-1] == " ":
        new = new[:-1]

print(new)

