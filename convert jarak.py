# input
nominal jarak = float(input())
dari = input()
ke = input()

#proses
hasil = None
if dari == "mil":
    if ke == "yard":
        hasil = nominal jarak*1760
    elif ke == "inchi":
        hasil = nominal jarak*63360
    elif ke == "kilometer":
        hasil = nominal jarak*1.609
    elif ke == "centimeter":
        hasil = nominal jarak*160934
    else:
        ValueError
elif dari == "yard":
    if ke == "mil":
        hasil = nominal jarak*0.0005682
    elif ke == "inchi":
        hasil = nominal jarak*36
    elif ke == "kilometer":
        hasil = nominal jarak*0.0009144
    elif ke == "centimeter":
        hasil = nominal jarak*91.44
    else:
        ValueError
elif dari == "kilometer":
    if ke == "mil":
        hasil = nominal jarak*0.6214
     elif ke == "yard":
        hasil = nominal jarak*1094
    elif ke == "inchi":
        hasil = nominal jarak*39370
    elif ke == "centimeter":
        hasil = nominal jarak*100000
    else:
        ValueError
elif dari == "inchi":
    if ke == "mil":
        hasil = nominal jarak*0.00001578
     elif ke == "yard":
        hasil = nominal jarak*0.02778
    elif ke == "kilometer":
        hasil = nominal jarak*0.0000254
    elif ke == "centimeter":
        hasil = nominal jarak*2.54
    else:
        ValueError
elif dari == "centimeter":
    if ke == "mil":
        hasil = nominal jarak*0.000006214
     elif ke == "yard":
        hasil = nominal jarak*0.01094
    elif ke == "kilometer":
        hasil = (nominal jarak*0.00001
    elif ke == "inchi":
        hasil = nominal jarak*0.3937
    else:
        ValueError
else:
    ValueError

#output
print(hasil)
