import math

num = int(input("enter a number: "))

fact = 1
i = 1
while True:
    fact = fact * i
    i += 1
    if num == fact:
        print("number is a factorial")
        break
    elif num < fact:
        print("number is not a factorial.")
        break
