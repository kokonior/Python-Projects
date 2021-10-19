print("Letak kuadran sebuah titik (x,y)")
x=int(input("x: "))
y=int(input("y: "))

if x>0:
    if y>0:
        print("Kuadran 1")
    elif y<0:
        print("Kuadran 4")
    else:
        print("Di antara kuadran 1 dan 4")
elif x<0:
    if y>0:
        print("Kuadran 2")
    elif y<0:
        print("Kuadran 3")
    else:
        print("Di antara kuadran 2 dan 3")
elif x==0:
    if y>0:
        print("Di antara kuadran 1 dan 2")
    elif y<0:
        print("Di antara kuadran 3 dan 4")
    else:
        print("Titik 0,0")
