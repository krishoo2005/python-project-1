#day11 functions and dictionaries code basic level

def show_skills(skills):
    print("\n...my skills...")
    for skill , level in skills.items():
        print(skill,"*",level,"/10")

def average_skill(skills):
    total = 0
    for level in skills.values():
        total = total + level
    avg = total / len(skills)
    return avg 


def best_skills(skills):
    top_skill = ""
    top_level = 0
    for skill , level in skills.items():
        if level > top_level:
            top_level = level
            top_skill = skill
    return top_skill , top_level

skills = {"python": 8, 
          "aws ec2 ":9,
          "linux":8,
          "ubuntu tier server":5,
          "cloud intern engg ":7
          }

show_skills(skills)

avg = average_skill(skills)
print("\n Average skill level",avg)

skill_name , skill_level = best_skills(skills)
print("best skill :",skill_name,"with level",skill_level)

