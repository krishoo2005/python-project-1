# Bubble Sort   code 
arr = [7, 0, 5, 8, 5 ,2 , 3, 9 , 9, 4 , 8]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
