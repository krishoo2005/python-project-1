arr1 = list(map(int,input("enter first array").split()))
arr2 = list(map(int,input("enter the second array").split()))

result = []

for i in range(len(arr1)):
    result.append(arr1[i] + arr2[i])

print("sum of array",result)    