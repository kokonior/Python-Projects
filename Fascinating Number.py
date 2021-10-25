'''
Write a Program in Python to input a number and check whether it is a Fascinating Number or not.

Fascinating Numbers: Some numbers of 3 digits or more exhibit a very interesting property. The property is such that, when the number is multiplied by 2 and 3, and both these products are concatenated with the original number, all digits from 1 to 9 are present exactly once, regardless of the number of zeroes.

Let's understand the concept of Fascinating Number through the following example:
Consider the number 192
192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
Concatenating the results: 192 384 576
It could be observed that '192384576' consists of all digits from 1 to 9 exactly once. Hence, it could be concluded that 192 is a Fascinating Number. Some examples of fascinating Numbers are: 192, 219, 273, 327, 1902, 1920, 2019 etc.
'''

#Function Opens-----------------------------
def isFascinating(num1 : int) -> bool:
	num2 = num1 * 2
	num3 = num1 * 3
	num = str(num1) + str(num2) + str(num3)
	
	digits = set()
	for each in num:
		if each == '0':
			continue
		if each in digits:
			break
		digits.add(each)	
	else:
		if len(digits) == 9:
			return True
			
	return False
#Function Closes----------------------------

num1 = int(input("Enter Number To Check:"))

if isFascinating(num1):
	print(f"Your Given Number {num1} Is A Fascinating Number.")

else:
	print(f"Your Given Number {num1} Is Not A Fascinating Number.")
