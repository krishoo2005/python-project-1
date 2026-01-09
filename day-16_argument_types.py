
def typesOfArguments(arguments_types):
    print(f"types of arguments --{arguments_types}")

typesOfArguments("positional_arguments, keyword_arguments ,default_arguments")



#  positional arguments 
def hello(a = 10,b = 20):
    
    print(a + b)
hello()





#keyword arguments


def oyye(name = "bob"):
    print(f"oyye {name}")
oyye("krushna")    





#default arguments

def hello(name , age):

    print(f"hiii {name} your age is {age}.")

hello("krushna " , 21)



