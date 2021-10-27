def to_float(x):
	
	# Mantissa
	b = x & (0xFFFFFFFF >> 9)
	m = 0
	for i in range(23):
		n = (x >> i) & 1
		m += n * 1 / (2**23 >> i)
	
	# Eksponen
	e = ((x >> 23) & (0xFFFFFFFF >> 24)) - 127
	
	# Sign
	sgn = x >> 31
	
	return (-1)**sgn * (1 + m) * 2**e
	
print("0xDA1F7000 =", to_float(0xDA1F7000))