def intro():

    nama = str(input("Siapa nama anda?"))
    crush = "shofa"

    if nama == crush:
        print("Hi, Iloveyou <3")
    elif nama == "Shofa":
        print("Hi, Iloveyou <3")
    else:
        print("Gausah bohong")

intro()

print("--------------------")

def iam():

    me = "salman" or "Salman" 

    print("Remember me?")
    ask = str(input("Who am i?"))
    if ask == me:
        print("Bener :)")
    else:
        print("Masa lupa :)")


iam()

print("--------------------")

def apolo():

    print ("Maaf, buat yang kemarin - kemarin.")
    answer = str(input("Jawab :"))
    if answer == "muhun" or "Muhun":
        print ("Nuhun, bby <3")
    elif answer == "iya" or "Iya":
        print ("Makasih")
    elif answer == "keun" or "Keun":
        print ("Iya :)")
    else:
        print ("Oh, Oke nuhun fa maaf ganggu :)")

apolo()

def balikan():
    
    print("Shofa masih aya rasa keneh teu ka Salman?")
    print("Mun aya Salman hayang siga dulu deui")
    print("Tapi lamun shofa tos balikan deui jeung si itu mah mangga")
    print("Keputusan aya di tangan Shofa")
    print("Dulu Salman kitu pedah asa dianggap herey")
    print("Salman lain teu nganggap Shofa")
    print("Tapi eta temen satongkrongan")
    print("Tos tarerangen da barudak ge bahwa abi balikan")
    print("Ayeuna mah terserah sofa, keputusan aya di Sofa")
    print("Jawab ngan Muhun/Moal")
    jawaban = str(input("Abi hoyong balikan :"))
    
    if jawaban == "muhun" or "Muhun":
        print("SS ieu terus send ka Salman :D")
    else:
        print("Muhun mangga eta mah terserah Shofa.")
        print("Hampura Salman tos nyia2keun Shofa nu kamari.")

balikan()