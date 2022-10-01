# solving the quadratic equation ax**2 + bx + c = 0

# importing math python package
import math

# taking user input
print("quadratic equation: ax**2 + bx + c = 0 ")
a = int(input("enter coefficient of x**2 or a "))
b = int(input("enter coefficient of x or b "))
c = int(input("enter the number c "))

# calculating the discriminant
d = (b**2) - (4*a*c)

# find two solutions
ans1 = (-b-math.sqrt(d))/(2*a)
ans2 = (-b+math.sqrt(d))/(2*a)

print('The solution are {} and {}'.format(ans1,ans2))