def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run():
    low = likelihood()
    print(f"Minimum likelihood of falling: {low}% where {low} is a value called by the previous function")


run()

