# game development - snake, water, gun
import random

round = 5
c= 0
u = 0

print(f"This is a {round} round game:\nSelect any one between snake, water and gun")

while round > 0:
    choices = ["snake","water","gun"]

    comp = random.choice(choices)
    user = input("Select any one: s for snake,w for water or g for gun")

    if (comp == "snake" and user == "s") or (comp == "water" and user == "w") or (comp == "gun" and user =="g"):   
        print(f"you chose {user} and comp chose {comp}")
        print("Draw")
        pass
    elif (comp == "snake" and user == "w") or (comp == "water" and user == "g") or (comp == "gun" and user == "s"):
        print(f"you chose {user} and comp chose {comp}")
        c += 1
        print("comp won")
    elif (comp == "snake" and user == "g") or (comp == "water" and user == "s") or (comp == "gun" and user == "w"):
        print(f"you chose {user} and comp chose {comp}")
        u += 1
        print("you won")
    else:
        print("incorrect choice")
    
    round -= 1
if u > c:
    print(f"You won by {u} rounds")
elif c>u:
    print(f"computer won by {c} round")
else:
    print("Both are equal")