def selection_sort(arr):  
    n = len(arr)
    
    for i in range(n):
        # cari nilai elemen terendah yang masih tersedia
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # tukar dengan nilai elemen ke-i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
  
unordered = [99, 55, 22, 11, 44]
print(selection_sort(unordered))