#lambda one line code for simple operation


# addition = lambda a ,b : a+b 
# print(addition(10,20))


# addition = lambda a:"even" if a % 2 == 0 else "odd"
# print(addition(12))


# filter

a = [2,3,4,5,6,7,25,22,45,52,25,52,52,25]
even = filter(lambda x:True if x%2 == 0 else False,a)
print(list(even))