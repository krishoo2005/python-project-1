print("krushna menu system")
while True:
    print("\n===MENU===")
    print("1.grade calculator")
    print("2. table printer")
    print("3 exit")

    choice = input("enter choice (1-3):")

    if choice == "1":
       print("grade calculator mode")
    elif choice == "2":
       print("table orinter mode ")
    elif choice == "3":  
        print("thnaks goodbye")
        break
    else:
        print("Invalid Choice")
