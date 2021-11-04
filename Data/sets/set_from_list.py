def observed():
    observation = []
    for item in range(7):
        print("Please Enter Observation:")
        observation.append(input())
    return observation


def run():
    print("Counting observations...")
    found_list = observed()
    new_set = set()
    for item in found_list:
        found_tuple = (item, found_list.count(item))
        new_set.add(found_tuple)

    for found_tuple in new_set:
        print(f"{found_tuple[0]} observed {found_tuple[1]} times")


run()


