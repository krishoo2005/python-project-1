print("welcome to krushna grade calculator")
name = input("enter your name :")
marks = int(input("enter your marks out of 100 :"))

print("\nstudent:",name)
print("marks:",marks)

if marks >= 90:
    grade = "a+"
elif marks >= 80:
    grade = "b+"
elif marks >= 70:
    grade = "c+"
elif marks >= 60:
    grade = "e+"    
else:
    grade = "fail"
     
print("grade =",grade)
