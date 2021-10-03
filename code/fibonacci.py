d1 = 0
d2 = 1

n = int(input("Masukkan batas deret : "))
for i in range(n):
  print(d1, end=' ')
  cn = d2 + d1
  d1 = d2
  d2 = cn
