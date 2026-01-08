import random
num = random.randint(1,10000)
tries = 0
while True:
    guess = int(input("gives one number - : "))
    if num == guess:
        tries += 1
        print(f"you choose correct guess number {num} ")
    elif num > guess:
        tries +=1
        print("please go higher ")
    elif num < guess:
        tries +=1
        print("please go lower")
    else:
        tries +=1
        print("yoou chooose wrong")
       
