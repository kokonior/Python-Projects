# random password generator 
import random

length=int(input("Enter the length of the password: "))

chars = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
for i in range(length):
    password += random.choice(chars)  
print(password)
