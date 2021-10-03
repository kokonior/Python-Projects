---
title: isprime
tags: math, beginner
---

Check if a number is prime

- Loop from 2 to square root of the number to check if it is prime

```py
def isprime(num):
    prime = True # Number is initially prime
    if num > 1:
        for i in range(2, num): # Loop each possible value
            if num % i == 0: # If number is divisible by this value
                prime = False # Number is no longer prime
                break
    return prime # Return if number is prime
```

```py
isprime(5) # True
```
