n = int(input("Enter how many numbers: "))

even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count =", even_count)
print("Odd numbers count =", odd_count)
