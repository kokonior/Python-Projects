# LUAS LINGKARAN (RETURN)
print("====LUAS JAJAR GENJANG====")
def Luas_Lingkaran(r):
    return 3.14 * (r * r)
 
r = float(input('Masukan jari-jari lingkaran: '))
luas = Luas_Lingkaran(r)
 
print('Luas Lingkaran: {}'.format(luas))
