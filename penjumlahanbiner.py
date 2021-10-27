def biner(n):
	b = ''
	while n  > 1:
		b = str(n % 2) + b
		n //= 2
	b = str(n%2) + b
	return b

def desimal(n):
	d = 0
	for i in range(len(n)):
		d = int(n[~i]) * 2**i + d
	return d
	
def jumlahBiner(a, b):
	a = '0'*(abs(len(a) - len(b))+1) + a
	b = '0'*(abs(len(a) - len(b))) + b
	carry = 0
	hasil = ''
	for i in range(len(a)-1, 0, -1):
		p = int(a[i])
		q = int(b[i])
		jumlah = (p ^ q) ^ carry
		carry = (p & q) | carry
		hasil = str(jumlah) + hasil
	hasil = (str(carry) + hasil).lstrip('0')
	return hasil

a = biner(16)
b = biner(16)
jumlah = jumlahBiner(a, b)
print(desimal(jumlah))
