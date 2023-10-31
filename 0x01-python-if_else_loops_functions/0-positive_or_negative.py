#!/usr/bin/python3
import random
n = random.randint(-20, 20)
if n > 0:
    print(f"{n} is positive")
elif n < 0:
    print(f"{n} is negative")
else:
    print(f"{n} is zero")
