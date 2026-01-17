# #inheritence {oops types}

# #position comes from heir  
# #it allow class 
# #oraganised structure

# class Factorymumbai:#parent class/supper class
#     a = "i am attribute mentioned inside factory"
#     def hello(self):
#         print("hello i am method mentioned inside factory ")


# class Factorypune(Factorymumbai):  #child classs / subclass 
#     pass


# obj = Factorymumbai()
# obj2 = Factorypune()
# print(obj2.hello())


class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your  animal name is {self.name}") 

class human(Animal):
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"hello your  name is {self.name} ,your age is {self.age}") 


person11 = human("krushna" ,23)
person1 = Animal("lion")

person1.show()
person11.show()
