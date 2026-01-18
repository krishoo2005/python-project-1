#abstraction is hide essentialdetails only show essential features

# using @abstractmethod
from abc import ABC, abstractmethod
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class square(abstract):
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        print("perimeter i have created",4*self.side)   #ye perimeter aur area dono decorator use kiya isliy complusory define karne pade.

    def area(self):
        print("area is ",self.side * self.side)

obj = square(5)
obj.perimeter()
obj.area()

#abstraction mai na hum class ke andar na decorator use karte hai jo function ka behaviour chnage karata hai..
#isliye function ke andar humne abstract method use karke ek complusory format banaya jo def karne ke wakt def hona chaiyiye tabhi decorator wwork karega ..
#output is :
#  perimeter i have created 20
#area is  25
     


        
