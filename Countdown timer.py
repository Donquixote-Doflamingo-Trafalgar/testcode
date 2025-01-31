import time
Seconds = int(input("How many seconds? "))
for x in range(Seconds, 0 , -1):
    sec = x % 60
    Minutes = int(x / 60) % 60
    hours = int(x / 3600) 
    print(f"{hours:02}:{Minutes:02}:{sec:02}")
    time.sleep(1)
print("Time the freakin up!")