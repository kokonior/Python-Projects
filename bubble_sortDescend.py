def bubble_sort(arr):
    # jumlah panjang list
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            # membandingkan masing" elemen
            # jika ingin mengurutkan dari terbesar ganti "<" kalo dari terkecil ">"
            if arr[j] < arr[j + 1]:
                # jika lebih besar, tukar.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


unordered = [7, 5, 4, 9, 8, 2, 1, 6]
print(bubble_sort(unordered))
