#reverse a number using recursion

def reverse_number(num):
    if num == 0:
        return

    print(num % 10, end="")
    reverse_number(num // 10)


num = int(input("Enter a number: "))
print("Reversed number:", end=" ")
reverse_number(num)
