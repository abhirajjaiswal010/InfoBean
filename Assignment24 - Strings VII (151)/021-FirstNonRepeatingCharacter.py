# 21. Find the first non-repeating character.

s=input("Enter The String : ")
# ch=input("Enter The character : ")
# new=""

# for i in s:
    
#     count=0
#     for j in s:
#         if i==j:
#             count+=1

#     if count==1:
#         new+=i
    
# # print(new)
# print(new[0])



freq={}

for i in s:

    freq[i]=freq.get(i,0)+1

print(freq)

for key,value in freq.items():
    if value==1:
        print(key)
        break
        
