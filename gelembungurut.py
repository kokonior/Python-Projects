def bubble_sort(angka: list) -> list:
    for item in angka:
        for i in range(len(angka)-1):
            if angka[i] > angka[i+1]:
                angka[i], angka[i+1] = angka[i+1], angka[i]

number = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_sort(number)
print(number)
print('HACKTOBERFEST')
