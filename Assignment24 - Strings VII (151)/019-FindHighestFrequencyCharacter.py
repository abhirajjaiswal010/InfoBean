# 19. Find the highest frequency character in a string.

s=input("Enter The String : ")
# ch=input("Enter The Character : ")
# freq=0
# char=""
# for i in s:
#     count=0
#     for j in s:
#         if i==j:
#             count+=1
    
#     if count>freq:
#         freq=count
#         char=i

# print(freq,char)

freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

high = 0
highC = ""

# key = character, value = frequency
for key, value in freq.items():

    if value > high:
        high = value
        highC = key

print(highC)
print(high)