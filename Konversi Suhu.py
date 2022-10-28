#program konvrensi celcius ke satuan lain

print("\nProgram Konvrersi Tempratur Celcius\n")
celcius = float(input("Masukan Suhu Dalam Celcius = "))

reamur = 4/5 * celcius
print("Suhu Reamur = ", reamur, "Reamur")

fahrenheit = 9/5 * celcius + 32
print("Suhu Fahrenheit = ", fahrenheit, "fahrenheit")

kelvin = 273 + celcius
print("Suhu Kelvin = ", kelvin, "kelvin")

#program konvrensi fahrenheit ke satuan lain
print("\nProgram Konvrersi Tempratur Fahrenheit\n")
fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit = "))

celcius = 5/9 * (fahrenheit-32)
print("Suhu Celcius = ", celcius, "Celcius")

reamur = 4/9 * (fahrenheit - 32)
print("Suhu Reamur = ", reamur, "Reamur")

kelvin = (fahrenheit-32) * (5/9) + 273.15
print("Suhu Kelvin = ",kelvin,"Kelvin")

#program konvrensi kelvin ke satuan lain
print("\nProgram Konvrersi Tempratur Kelvin\n")
kelvin = float(input("Masukan Suhu Dalam Kelvin = "))

celcius = kelvin - 273
print("Suhu Celcius = ", celcius, "Celcius")

reamur = 4/5 * (kelvin - 273)
print("Suhu Reamur = ", reamur, "Reamur")

fahrenheit = (kelvin - 273.15) * (9/5) + 32
print("Suhu Kelvin = ",fahrenheit,"Fahrenheit")

#program konvrensi reamur ke satuan lain
print("\nProgram Konvrersi Tempratur Reamur\n")
reamur = float(input("Masukan Suhu Dalam Reamur = "))

celcius = 5/4 + reamur
print("Suhu Celcius = ", celcius, "Celcius")

fahrenheit = 9/4 * reamur + 32
print("Suhu Reamur = ", fahrenheit, "Reamur")

kelvin = 5/4 * reamur + 273
print("Suhu Kelvin = ",kelvin,"Fahrenheit")
