class Factory():
    def __init__ (self,college,student,idcard):#construtor init is basically run automatically when we call the class .and it target the location
       self.college = college
       self.student = student 
       self.idcard = idcard


       #isse bhi hum function ko access kar skate hai ..
    def show(self):
        print(f"the objects are -{self.college} , {self.student} , {self.idcard} ")
       
krushna = Factory("csmss" , "krushna" , 3136) 
ak = Factory("csmss" , "akash" , 0000)
print(krushna.idcard) 
print(f"name of student is - {ak.student}") #like this way we also print 

krushna.show() #function calling 

