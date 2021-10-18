def leftRightArrowsPattern(rows):
    r, r1, c, row1 = None, None, None, None
    row1 = rows
    rows = rows * 4

    print ("\n----Panah Ke Kanan-----\n")
    for r in range (1, rows):
        # to print the left arrow
        if r <= row1:
            for c in range (1, (row1 - r) + 1):
                print (end=" ")
            for c in range (r, row1 + 1):
                print (end="*")
            print (end="\n")

        if r > row1 and r <= row1 * 2:
            for c in range (1, (r - row1) + 1):
                print (end=" ")
            for c in range (1, (r - (row1 - 1)) + 1):
                if (r - row1) < row1:
                    print (end="*")
            print (end="\n")

        
        if r > row1 * 2 and r <= row1 * 3:
            if r == (row1 * 2) + 1:
                print ("\n----Panah Ke Kiri-----\n")
            for c in range ((r - 1) - (row1 * 2), 0, -1):
                print (end="  ")
            for c in range ((3 * row1) - (r - 1), 0 ,-1):
                print (end="*")
            print (end="\n")

        if r > row1 * 3:
            for c in range ((row1 * 4) - (r + 1), 0, -1):
                print (end="  ")
            for c in range ((r + 1) - (3 * row1), 0 , -1):
                print (end="*")
            print (end="\n")

print ("-----Masukan Panjangnya arah panah-----")
rows = int (input ())

if rows > 0:
   
    leftRightArrowsPattern(rows)
