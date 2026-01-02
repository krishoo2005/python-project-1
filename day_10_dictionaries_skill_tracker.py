print("\nday 10 dictionaries & skill tracker ")
skills = { "python":8,
            "github":7,
            "flask":5,
            "arduino":9
}
print("\ncurrent skill ratings:\n")
print("*"*25) #star ki line print hogi

#for loop

for skill_name, rating in skills.items():
    print(f"{skill_name}:{rating}/10")

print(f"\ntotal skills :{len(skills)}")


#add new skills like append 
skills["backend developer"]=6
print(f"\nadded backend developer:{len(skills)}")

#update rating 
skills["python"]=9
print(f"python upgraded:{skills['python']}")


#remove skill flsk
if "flask" in skills:
    del skills["flask"]
print("\n flask removed (practice more)")

#final list
print("final list")
for s in skills:
    print(f"{s}:{skills[s]}")

#challenge :average 
total = sum(skills.values())
avg = total / len(skills)
print(f"\naverage:{avg}/10")
print(f"\n total {sum(skills.values())}")

if avg >= 9:
    print("\nbe consistent ")
else:
    print("Need more discipline in study")    