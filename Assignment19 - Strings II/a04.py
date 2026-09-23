'''
Docstring for a04
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5

'''
# n=input("Enter The Complaint : ")
# count=0

# for word in n.split():
#     # print(word)
#     count+=1

# print(count)


n = input("Enter The Complaint : ")

count = 0
i = 0

while i < len(n):
    if n[i] != " ":
        if i == 0 or n[i - 1] == " ":
            count += 1
    i += 1

print(count)

#algo
#1. agar ch vo space nhi hai 
#2. phir check ki i=0 mein ch  hai toh count++
#3. and agar ch ke pehle space hai toh count++