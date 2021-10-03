# Menyelesaikan persamaan kuadrat ax2 + bx + c = 0

# import module matematika math
import math

# Input koefisien dari keyboard
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

# hitung diskriminan d
d = (b**2) - (4*a*c)

# menemukan x1 dan x2
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)

print('Solusinya adalah {0} dan {1}'.format(x1, x2))
