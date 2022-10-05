import string
import random

def generate(length=10):
    char = string.ascii_letters
    res = ''
    for i in range(int(length)):
        res += random.choice(char)
    return res

length = input('Length : ')
res = generate(length=length)
print(res)
