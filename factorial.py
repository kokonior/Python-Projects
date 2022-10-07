import math


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


number = int(input("input number factorial :"))
print(factorial(number))


if number >= 0:
    print(math.factorial(number))
else:
    print("value is invalid")
