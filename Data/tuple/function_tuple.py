def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    low, high = likelihood()
    print(f"Minimum likelihoods of falling: {low}%")
    print(f"Maximum likelihood of falling: {high}%")


run()

