# health management system

action = input("Write action: log or retrieve\n")
name = input("enter name : harry, rohan or hammad\n")
process = input("enter process: food or exercise\n")

def getdate():
    import datetime
    return datetime.datetime.now()

if action == "log":
    if name == "harry":
        if process == "food":
            f = open("harry_food.txt","a")
            date = getdate()
            food = input("enter the food")
            f.write(f"[{date}] - {food}\n")
            print("food is added")
            f.close()
        elif process == "exercise":
            f = open("harry_exer.txt","a")
            date = getdate()
            exercise = input("enter the exercise")
            f.write(f"{date} - {exercise}\n")
            print("exercise is added")
            f.close()
        else:
            print("select the correct process")
            
    elif name == "rohan":
        if process == "food":
            f = open("rohan_food.txt","a")
            date = getdate()
            food = input("enter the food")
            f.write(f"{date} - {food}\n")
            print("food is added")
            f.close()
        elif process == "exercise":
            f = open("rohan_exer.txt","a")
            date = getdate()
            exercise = input("enter the exercise")
            f.write(f"{date} - {exercise}\n")
            print("exercise is added")
            f.close()
        else:
            print("select the corrext process")
            
    elif name == "hammad":
        if process == "food":
            f = open("hammad_food.txt","a")
            date = getdate()
            food = input("enter the food")
            f.write(f"{date} - {food}\n")
            print("food is added")
            f.close()
        elif process == "exercise":
            f = open("hammad_exer.txt","a")
            date = getdate()
            exercise = input("enter the exercise")
            f.write(f"{date} - {exercise}\n")
            print("exercise is added")
            f.close()
        else:
            print("select the correct process")
    else:
        print("select the correct name")
        
elif action == "retrieve":
    if name == "harry":
        if process == "food":
            f = open("harry_food.txt")
            for i in f:
                print(i,end="")
            f.close()
        elif process == "exercise":
            f = open("harry_exer.txt")
            for i in f:
                print(i,end="")
            f.close()
        else:
            print("select the correct process")
            
    elif name == "rohan":
        if process == "food":
            f = open("rohan_food.txt")
            for i in f:
                print(i,end="")
            f.close()
        elif process == "exercise":
            f = open("rohan_exer.txt")
            for i in f:
                print(i,end="")
            f.close()
        else:
            print("select the corrext process")
            
    elif name == "hammad":
        if process == "food":
            f = open("hammad_food.txt")
            for i in f:
                print(i,end="")
            f.close()
        elif process == "exercise":
            f = open("hammad_exer.txt")
            for i in f:
                print(i,end="")
            f.close()
        else:
            print("select the correct process")
    else:
        print("select the correct name")
        
else:
    print("select the corrct action")