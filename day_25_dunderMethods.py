#dunders methods 
#star and end with double underscore 

#automatiically get called when you perform certain action on objects

# for example __init__  __add__  __str__


class animal:
    def __init__(self,name,age ):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"hello {self.name} how are youu " 
    
    # def __add__(self,other):
    #     return f"you sum of ages are = {self.age + other.age}"
# /jar object 2 peksha jast asle an sum karyachi asli t for loop use karane 
    
    def __add__(self,other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f"sum of age is {self.age + sum}"



obj = animal("lion" , 35) 
obj2 = animal("cheetah" , 15) 
obj3 = animal("deer" , 20)
# print(obj)
# print(obj2)
print(obj + (obj2,obj3))
