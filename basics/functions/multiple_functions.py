def display_ladder(steps):
  for step in range(steps):
    print("|_|")
  print("| |")


def create_ladder():
  print("How many steps do you want on your ladder?")
  input1 = int(input())
  display_ladder(input1)

create_ladder()