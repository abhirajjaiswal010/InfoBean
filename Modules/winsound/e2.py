import winsound
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

winsound.Beep(1000, 1000)

print("Time's up!")