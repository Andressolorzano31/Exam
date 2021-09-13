age = input("How old are you?\n")
len_age=len(age)
if len_age == 2:
    print(f"You have {age[0]} decades and {age[1]} years")
elif len_age == 1:
    print(f"You have {age[0]} years")
elif len_age == 3:
    print(f"You have {age[0]} centuries,{age[1]} decades and {age[2]} years")
else:
    print("Are you a Alien?")

