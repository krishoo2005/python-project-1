

def decorators(func):

    def wrapper(*args,**kwargs):
        print("the addtion of your number is ")
        func(*args,**kwargs)
        print("thank youhh i hope uh like it ")
    return wrapper

def addition(*args ):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum) 

print(f"your addition is ")
addition(10,2)

def addition(**kwargs ):
    
    
        print("your imformation is \n")       
        for i in kwargs:
            print(f"{i}:{kwargs[i]}")
            
addition(name = "krushna", designation = "student" , age = 21)
