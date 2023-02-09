from calendar import c
import random
import time

countdown = random.randint(1,5)

while countdown >= 1:
    print(countdown)
    time.sleep(1)
    if countdown == 1:
        print("START")
    countdown -= 1
