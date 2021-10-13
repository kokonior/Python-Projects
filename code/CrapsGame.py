count = 1

while True :

    total = 0
    a1 = int(input())
    a2 = int(input())
    a = a1+a2
    total = total+a

    if (a1 >= 1 and a1 <= 6) and (a2 >= 1 and a2 <= 6 ) :
        if  (total == 7 or total == 11 ) and count == 1 :
            result = 'W'
            break

        if (total == 2 or total == 3 or total == 12 ) and count == 1 :
            result = 'L'
            break

        if (total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10 ) and (count == 1) :          
            target = total

        if total == 7 and count > 1 :
            result = 'L'
            break

        if (total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10 ) and (count > 1) :
            if (total == target) and count > 1 :
                result = 'W'
                break

        count = count+1

    if  (a1 < 1 or a1 > 6) or (a2 < 1 or a2 > 6 ) :
        print("ERROR")

print("%d %d %s"%(count,total,result))      
