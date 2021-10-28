def movements():
  path = []
  path.append("Move Forward")
  path.append(10)
  path.append("Move Backward")
  path.append(5)
  path.append("Move Left")
  path.append(3)
  path.append("Move Right")
  path.append(1)
  return path


def run():
  print("Moving...")
  pathfound = movements()
  print(pathfound[0], "for",
  pathfound[1] ,"steps")
  print(pathfound[2],"for", pathfound[3],"steps")
  print(pathfound[4],"for",pathfound[5],"steps")
  print(pathfound[6],"for",pathfound[7],"steps")



run()