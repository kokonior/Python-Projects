ukuran_catur = int(input('Masukkan Ukuran Catur : '))
list2D = []

#Papan Catur
print('Masukkan papan catur:')
for n in range(ukuran_catur):
    isi_string = input()
    isi_list = isi_string.split()
    list2D.append(isi_list)

#Posisi Benteng
for i in range(ukuran_catur):
    for j in range(ukuran_catur):
        if list2D[i][j] == 'R':
            posisi_X = i
            posisi_Y = j

hasil = 0

try:
    for s in range(len(list2D)):
        if list2D[posisi_X+s][posisi_Y] == 'P':
            hasil += 1
        if list2D[posisi_X][posisi_Y+s] == 'P':
            hasil += 1    
        if list2D[posisi_X-s][posisi_Y] == 'P':
            if posisi_X-s >= 0:
                hasil += 1
        if list2D[posisi_X][posisi_Y-s] == 'P':
            if posisi_Y-s >= 0:
                hasil += 1
except IndexError:
    pass

print("Banyaknya pion catur yang dapat dimakan benteng:")
print(hasil)