def directions():
    directions = []
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn left")
    directions.append("Turn Right")
    return directions

def menu():
    print("Please select a direction:")
    foundlist = directions()
    counter = 0
    for line in foundlist:
        print(f"{counter} : {line}")
        counter += 1
menu()

