def makepattern(d):
 rows = d
 num = rows
 for i in range(rows, 0, -1):
     for j in range(0, i):
         print(num, end=' ')
     print("\r")
Enternum=int(input("Please enter the number to make its inverted pyramid pattern"))
makepattern(Enternum)
