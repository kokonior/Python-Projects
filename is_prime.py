import sys
import math


def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True


# To run the code, just enter "python is_prime.py <num>" replacing <num> by any integer
# Example: python is_prime.py 11
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please inform a number')
    else:
        num = int(sys.argv[1])

        if is_prime(num):
            print(f'{num} is prime!')
        else:
            print(f'{num} is NOT prime!')

