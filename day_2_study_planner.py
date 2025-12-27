print("welcome to krushna study planner ")
name = input("enter your name = ")
day = input("enter day of the week = ")

print("\nHello",name + "!")
print("todays plan:\N")

if  day.lower() in ["monday","tuesday","wednesday","thursday","friday"]:
    print("1 hour=resoning or aptitude \n ")
    print("1 hour core electrical or JE preparation  \n")
    print("30minutes python basic code learning \n ")
    print("20 minutes book reading of self development book \n")
elif day.lower() in ["saturday","sunday"]:
    print("2hours full je syallabus revision and mock tesst")
    print("1hour pythonor projrct work ")
    print("relax or gym and family time ")
else:
    print("invalid day entered.please give correct input")  