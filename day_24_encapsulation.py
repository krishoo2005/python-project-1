

    #by using double underscore it make data private 
    #by single underscoe it make protected but we can access
    #by double underscore we can access within the functions
# class factory:    
#     __a = "krushna aghade"  

#     def show(self):
#         print(factory.__a)

# obj = factory()        
# obj.show()

class demo:
    __a =  "aghadepatil"  #(private and only use within a function )
    def __init__(self ):
        self.name = "krushna aghade"
        self._age = 21
        self.__salary = 35000

    def show1(self) :
        print("inside the class")   
        print("public", self.name)
        print("protected", self._age)#single underscore is protected same as protected 
    
        print("private", self.__salary)#private using double underscore 
        print(demo().__a)
class virtual(demo):
    def __init__(self , hero , age):
        self.hero = hero
        self.age = age
    def show(self):
        print(self.hero , self.age) 
        # print(super().__a)      

obj = demo()
obj.show1()     


obj = virtual("vaibhav" , 21)
obj.show()        