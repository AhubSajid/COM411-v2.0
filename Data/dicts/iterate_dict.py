def pattern():
    sequences = dict()
    sequences["Short Sequence"] = 3
    sequences["Medium Sequences"] = 2
    sequences["Long Sequences"] = 1
    return sequences


def display_keys(in_dict):
    print()
    print("Keys:")
    for key in in_dict.keys():
        print(key)


def display_values(in_dict):
    print()
    print("Values:")
    for values in in_dict.values():
        print(values)

def display_items(in_dict):
    print()
    print("Items:")
    for key, value in in_dict.items():
        print(f"{key}: {value}")



def run():
    print(pattern())
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


run()