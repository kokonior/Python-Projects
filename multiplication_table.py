def multiplication_table(num):
    for i in range(1, 11):
       print(num, 'x', i, '=', num*i)

n = int(input("Enter the number you want to find the table "))
multiplication_table(n)
