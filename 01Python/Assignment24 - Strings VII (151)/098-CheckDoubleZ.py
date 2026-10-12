# Input:  "pizza"
# Output: True

# Input:  "zebra"
# Output: False

# Input:  "fizz"
# Output: True

# Input:  "amazing"
# Output: False


s = input("Enter the string: ")

found = False

for i in range(len(s) - 1):
    if s[i] == 'z' and s[i + 1] == 'z':
        found = True
        break

print(found)