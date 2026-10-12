'''
Docstring for Assignment23 - String VI.a01
. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

```text
abcabcbb
```

Output:

```text
abc
```
'''

s = input("Enter: ")

ans = ""

# Har possible starting position se substring banana
for i in range(len(s)):

    # i se lekar last character tak different substring banayenge
    for j in range(i + 1, len(s) + 1):

        # Current substring nikalo
        sub = s[i:j]

        count = 0

        # Puri string mein check karo ki substring kitni baar present hai
        for k in range(len(s) - len(sub) + 1):

            # Maan rahe hain ki substring match karegi
            match = True

            # Current substring ke har character ko compare karo
            for m in range(len(sub)):

                # Agar character match nahi karta
                if s[k + m] != sub[m]:

                    # Substring match nahi hui
                    match = False
                    break

            # Agar complete substring match ho gayi
            if match:
                count += 1

        # Agar substring kam se kam 2 baar aayi
        # aur current answer se badi hai
        if count >= 2 and len(sub) > len(ans):

            # Current substring ko longest repeating substring bana do
            ans = sub

print(ans)


    
