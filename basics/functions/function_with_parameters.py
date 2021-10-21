def escape_by(plan) :
  if plan == "jumping over":
    print("We can't escape that way! The boulder is too big")
  elif plan == "running around":
    print("We cannot escape that way the boulder is too fast")
  elif plan == "going deeper":
    print("That might work! let's go deeper!")
  else:
    print("We can't escape that way! Boulder is in the way!")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")