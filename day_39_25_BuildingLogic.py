# Program 1: Sort numbers ascending
arr = [8, 3, 5, 1, 56 ,21 , 25  , 541545  ,2   ,6]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
