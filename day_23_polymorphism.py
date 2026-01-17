#polymorphism 1 name form are more 
#1name but work more in different form 

#duck typing method of morphism 


class animal():
    def show(self):
        print("\n1 showing the form of polymorphism\n ")


class human(animal):
    def show(self):
        print("2 same name but different form\n")  

obj = animal()
obj2 = human()         

obj.show()
obj2.show()
