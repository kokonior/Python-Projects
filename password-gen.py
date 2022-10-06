import random
import string

passlength=int(input("Enter your required password length:\n"))

lowerchars=string.ascii_lowercase
upperchars=string.ascii_uppercase
nums=string.digits
specialchars=string.punctuation

integrate=upperchars+specialchars+lowerchars+nums

volatile=random.sample(integrate,passlength)

newpassword="".join(volatile)

print(newpassword)

