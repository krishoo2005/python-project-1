#extract the ven numbers and count it 

n = 123689884864562478962154855
count = 0
even_digit = []

while n > 0:
    digit = n % 10
    
    if digit % 2 == 0:
       even_digit.append(digit)
       
       count  = count +1
       
    n = n // 10 

even_digit.reverse()

print(f"even digits are {even_digit}")

print("these are even numbers ",count)

