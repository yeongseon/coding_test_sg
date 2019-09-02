file = open("./input.txt")
lines = file.readlines()

def parseAdd(arr):
    return {"command":arr[0]}

def parseCharge(arr):
    return {"command":arr[0]}

def parseCredit(arr):
    return {"command":arr[0]}

commands = []
for line in lines:
    arr = line.replace("\n", "").split(" ")
    if arr[0] == "Add":
        commands.append(parseAdd(arr))
    elif arr[0] == "Charge":
        commands.append(parseCharge(arr))
    elif arr[0] == "Credit":
        commands.append(parseCredit(arr))

print(commands)


