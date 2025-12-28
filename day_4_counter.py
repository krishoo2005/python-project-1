print("Simple Counter Program")

limit = int(input("Enter a positive number: "))

current = 1

while current <= limit:
    print("Current number:", current)
    current = current + 1  # same as current += 1

print("Counting finished!")
