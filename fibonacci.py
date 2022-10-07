def recurFibonaci(number):
    if number <= 1:
        return number
    else:
        return recurFibonaci(number - 1) + recurFibonaci(number - 2)


numberTerms = 10
if numberTerms <= 0:
    print("enter positive integers")
else:
    print("fibonaci sequence ")
    for i in range(numberTerms):
        print(recurFibonaci(i))
