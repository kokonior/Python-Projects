#program to calculate final score 
print("Program untuk menghitung nilai akhir ")
#input score
nilai_tugas = float(input("Masukkan nilai dari tugas : "))
nilai_uts = float(input("Masukkan nilai dari UTS : "))
nilai_uas = float(input("Masukkan nilai dari UAS : "))
nilai_akhir = (0.50 * nilai_tugas) + (0.30 * nilai_uts) + (0.20 * nilai_uas)
#process
if nilai_akhir >= 95:
    print(nilai_akhir)
    print("A+")
    print("Lulus")
else:
    if nilai_akhir >= 90:
        print(nilai_akhir)
        print("A")
        print("Lulus")
    else:
        if nilai_akhir >= 85:
            print(nilai_akhir)
            print("B+")
            print("Lulus")
        else:
            if nilai_akhir >= 80:
                print(nilai_akhir)
                print("B")
                print("Lulus")
            else:
                if nilai_akhir >= 75:
                    print(nilai_akhir)
                    print("C+")
                    print("Lulus")
                else:
                    if nilai_akhir >= 70:
                        print(nilai_akhir)
                        print("C")
                        print("Lulus")
                    else:
                        print(nilai_akhir)
                        print("D")
                        print("Tidak Lulus")
