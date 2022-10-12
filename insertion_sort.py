def insertion_sort(arr):
     
    for i in range(1, len(arr)):
        # ini elemen yang akan kita posisikan
        key_item = arr[i]
        # kunci index posisi 
        j = i - 1
        # lakukan perulangan kedua
        while j >= 0 and arr[j] > key_item:
            # menggeser elemen yang lain
            arr[j + 1] = arr[j]
            j -= 1
        # memposisikan elemen
        arr[j + 1] = key_item

    return arr

unordered = [99, 55, 22, 11, 44]
print(insertion_sort(unordered))