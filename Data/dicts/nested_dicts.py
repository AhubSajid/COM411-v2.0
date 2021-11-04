def medium_pattern():
    pattern = dict()
    pattern["sequences"] = 111000
    pattern["occurrences"] = 25
    return pattern


def short_pattern():
    pattern = dict()
    pattern["sequences"] = 101
    pattern["occurrences"] = 5
    return pattern


def long_pattern():
    pattern = dict()
    pattern["sequences"] = 1100110011001100
    pattern["occurrences"] = 50
    return pattern


def run():
    print("Analysing patterns...")
    final_dict = dict()
