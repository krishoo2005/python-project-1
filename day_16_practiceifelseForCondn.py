"""emp = int(input("tell me your temperature :- "))
if temp > 30:
    print("its too hot")
elif temp <10:
    print("its too cold!..")    
elif temp < 30:
    print("its too cool ")    
"""
#for i in range(7,71,7):
 #    print(i)
"""n =  int(input("write table number :- "))
    
for n in range(n,n*10+1,n):
    print(n) 
    """

"""a = "krushna learning python basic."
print(len(a),"lentgh  ")

for i in range (len(a)):
    print(a[i])  
       
             """

"""
#for table print 
n = int(input("give me the table number :_"))

for i in range(7,71,7):
    print(i)  """

""" n = int(input("give me the table number :_"))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")
    """

"""
# sum of the number 
n = int(input("give me the number :_"))
sum = 0
for i in range(1,n+1):
    sum = sum + i 
print(f"you sum till {n} is  = {sum}") 


#finding factorial number 

n = int(input("give the factorial number = "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(f"The factorial of {n} is {fact}") """


#sum of odd and even number
"""
n = int (input("given the number "))

even = 0
odd  = 0
for i in range (1,n+1):
    
    if i%2 == 0:
       
       
       even = even + i

    
    else:
        
        odd = odd + i
        
print(f"your odd number sum is  = {odd} and even number sum is = {even}")"""

n = int (input("given the number "))
sum = 0
for i in range(1,n):
    if n%i == 0:
       sum = sum + i
if sum == n:
   print("number is perfect") 

else:
   print("number is not perfect") 

