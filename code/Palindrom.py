def cekpalindrom (teks) :
    list = []
    belakang = ''
    depan = ''
    indikator = True
    for i in range (len(teks)) :
        if teks[i] != ',' and teks[i] != '.' and teks[i] != "'" and teks[i] != '"' and teks[i] != '!' and teks[i] != '?' and teks[i] != ' ' :
            list.append(teks[i])
    while len(list) > 1 and indikator  :
        depan += list.pop(0)
        belakang += list.pop()
        if belakang != depan :
            indikator = False
    if indikator :
        print("kata ", teks, "adalah kata palyndrom.")
    else :
        print("kata ", teks, "bukan kata palyndrom.")


a = input('masukkan teks : ')

print('hasil : ')
cekpalindrom (a)
