def directions():
  direction = []
  direction.append("Move Forward")
  direction.append("Move Backward")
  direction.append("Turn left")
  direction.append("Turn Right")
  return direction


def menu():
    print("Please select a direction:")
    foundlist = directions()
    counter = 0
    counter1 = 0
    for line in foundlist:
      print(f"{counter} : {line}")
      counter += 1
    input1 = int(input())
    for line in foundlist:
      if counter1 == input1:
        return line
      else:
        counter1 += 1


def run():
  route = []
  print("Working out escape route...")
  counter2 = 0
  for counter2 in range(5):
    route.append(menu())

  print(f"Escape route:{route} where {route} is the content of the list route")



run()





