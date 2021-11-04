def pattern():
    sequences = dict()
    sequences["Short Sequence"] = 3
    sequences["Medium Sequences"] = 2
    sequences["Long Sequences"] = 1
    return sequences


def run():
    print(pattern())


run()