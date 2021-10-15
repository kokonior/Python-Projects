import random
import string
#enter length
print("***PASSWORD GENERATOR IS READY TO PASSWORD YOU*** \n")

passlength=int(input("Enter your required password length:\n"))

#assigning password characters
lowerchars=string.ascii_lowercase
upperchars=string.ascii_uppercase
nums=string.digits
specialchars=string.punctuation

#combining the random values
integrate=upperchars+specialchars+lowerchars+nums

#generating password using random 
volatile=random.sample(integrate,passlength)

newpassword="".join(volatile)

print(newpassword)

