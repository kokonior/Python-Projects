n = input("Enter temperature value: ")
sign = n[-1]
n = n[0:-1]
n = int(n)

# Celcius to:
if sign == "C" or sign == "c":

	# Reamur
	r = (4 / 5) * n
	r = round(r)

	# Kelvin
	k = n + 273
	k = round(k)

	# Fahrenheit
	f = (9 / 5) * n + 32
	f = round(f)

	print(str(r) + "R")
	print(str(k) + "K")
	print(str(f) + "F")

# Reamur to:
elif sign == "R" or sign == "r":

	# Celcius
	c = (5 / 4) * n
	c = round(c)

	# Kelvin
	k = c + 273
	k = round(k)

	# Fahrenheit
	f = (9 / 4) * n + 32
	f = round(f)

	print(str(c) + "C")
	print(str(k) + "K")
	print(str(f) + "F")

# Kelvin to:
elif sign == "K" or sign == "k":

	# Celcius
	c = n - 273
	c = round(c)

	# Reamur
	r = (4 / 5) * (n - 273)
	r = round(r)

	# Fahrenheit
	f = (9 / 5) * (n - 273) + 32
	f = round(f)

	print(str(c) + "C")
	print(str(r) + "R")
	print(str(f) + "F")

# Fahrenheit to:
elif sign == "F" or sign == "f":

	# Celcius
	c = (5 / 9) * (n - 32)
	c = round(c)

	# Reamur
	r = (4 / 9) * (n - 32)
	r = round(r)

	# Kelvin
	k = (5 / 9) + (n - 32) + 273
	k = round(k)

	print(str(c) + "C")
	print(str(r) + "R")
	print(str(k) + "K")

else:
	print("Enter the correct temperature")
