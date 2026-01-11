# a = [1,2,3]
# b = [1,2,3]
# print(a==b)
# print(a is b )

# #answer is True 
# #answer is false/
# squares = []
# for i in range(5):
#     squares.append(i * i)

# squares = [i * i for i in range(5)]
# print(squares)
# try:
#     x = 10 / 0
# except:
#     print("Error occurred")
# finally:
#     print("Program ended")


# add = lambda a,b :a+b
# print(add(9,6))


# def student(**kwargs):
#     print(kwargs)

# student(name="Krushna", age=20)

# def hi(*args):
#     return sum(args)

# print(hi(1, 2, 3))
class Student:
    def __init__(self, name):
        self.name = name
s = Student("ravi")
print(s.name)