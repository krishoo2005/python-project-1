def binary_search(arr, low, high, key):
    if low > high:
        return -1   # element not found
    
    mid = (low + high) // 2
    
    if arr[mid] == key:
        return mid
    
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    
    else:
        return binary_search(arr, mid + 1, high, key)


# Example
arr = [1, 3, 5, 7, 9, 11]
result = binary_search(arr, 0, len(arr)-1, 7)

print("Index:", result)
