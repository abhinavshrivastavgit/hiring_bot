skill = input("What is your primary tech skill? ")
projects = int(input("How many projects have you uploaded to GitHub? "))
if skill.lower()=='python' and projects > 3:
    print('"You are a Top Candidate for NVIDIA!"')
elif skill.lower()=='python' and projects<= 3:
    print('"Great skill! Build more projects to get noticed."')
else:
    print('"NVIDIA loves Python! Consider learning it to boost your profile."')