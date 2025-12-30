print("MULTIPLICATION TABLE PRINTER")
number = int(input("enter number of the table  = "))

print(f"\n Table of {number}:")        
print("=================")

for i in range (1,11): #1,2,3,4,....10
    result = number * i
   # print(f"{number} * {i:2d} = {result:3d}") or you print like 
    print( number,"*" , i , "=" , number*i)
