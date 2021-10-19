print("Letak kuadran sebuah titik")
x=int(input("x: "))
y=int(input("y: "))

if x>0:
    if y>0:
        print("Kuadran 1")
    elif y<0:
        print("Kuadran 4")
elif x<0:
    if y>0:
        print("Kuadran 2")
    elif y<0:
        print("Kuadran 3")
elif x==0:
    print("Titik 0,0")
