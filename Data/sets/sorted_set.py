def observed():
    observation = []
    for item in range(5):
        print("Please Enter Observation:")
        observation.append(input())
    return observation


def remove_observations(observation):
    print("Do you wish to remove observation (yes/no) ?")
    input1 = input()
    if input1 == "yes":
        print("Enter observation to be removed:")
        input2 = input()
        observation.remove(input2)
        print("Done!")
        remove_observations(observation)
    return observation


def run():
    found_list = observed()
    new_list = remove_observations(found_list)
    new_set = set()
    print()
    for item in found_list:
        found_tuple = (item, found_list.count(item))
        new_set.add(found_tuple)
    for item in new_set:
        print(f"{item[0]} observed {item[1]} times")


run()

