# Sorting numbers in descending order
arr = [31, 27, 21, 39, 862 ,70 ,58 ,52 ,39 ,94]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
