# input
suhu = float(input())
asal = input()
tujuan = input()

#proses
hasil = None
if asal == "Celcius":
    if tujuan == "Fahrenheit":
        hasil = suhu*1.8+32
    elif tujuan == "Kelvin":
        hasil = suhu+273.15
    elif tujuan == "Reamur":
        hasil = suhu*0.8
    elif tujuan == "Rankine":
        hasil = suhu*1.8+32+459.67
    else:
        ValueError
elif asal == "Fahrenheit":
    if tujuan == "Celsius":
        hasil = (suhu-32)/1.8
    elif tujuan == "Kelvin":
        hasil = (suhu+459.67)/1.8
    elif tujuan == "Reamur":
        hasil = (suhu-32)/2.25
    elif tujuan == "Rankine":
        hasil = suhu+459.67
    else:
        ValueError
elif asal == "Reamur":
    if tujuan == "Celcius":
        hasil = suhu*1.25
     elif tujuan == "Fahrenheit":
        hasil = suhu*2.25+32
    elif tujuan == "Kelvin":
        hasil = suhu*1.25+273.15
    elif tujuan == "Rankine":
        hasil = suhu*2.25+32+459.67
    else:
        ValueError
elif asal == "Kelvin":
    if tujuan == "Celcius":
        hasil = suhu-273.15
     elif tujuan == "Fahrenheit":
        hasil = suhu*1.8-459.67
    elif tujuan == "Reamur":
        hasil = (suhu-273.15)*0.8
    elif tujuan == "Rankine":
        hasil = suhu*1.8
    else:
        ValueError
elif asal == "Rankine":
    if tujuan == "Celcius":
        hasil = (suhu-32-459.67)/1.8
     elif tujuan == "Fahrenheit":
        hasil = suhu-459.67
    elif tujuan == "Reamur":
        hasil = (suhu-32-459.67)/2.25
    elif tujuan == "Kelvin":
        hasil = suhu/1.8
    else:
        ValueError
else:
    ValueError

#output
print(hasil)
