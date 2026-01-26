#counting even and odd number 
num = int(input("Enter a number: "))

even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    num = num // 10

print("Even digits count:", even_count)
print("Odd digits count:", odd_count)
