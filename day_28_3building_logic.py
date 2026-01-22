n=2002
hello = n
rev = 0

while n >0 :
    digit = n%10
    rev = rev *10 + digit
    n = n // 10

if hello == rev:
   print("number is palindrome")
else:
    print("not palindrome ")    