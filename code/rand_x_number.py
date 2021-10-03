from random import randint

def rand_x_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

digit = input('Digit: ')

try:
    int_digit = int(digit)
    print(rand_x_number(int_digit))
except:
    print('Invalid Digit')