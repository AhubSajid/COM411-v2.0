def search(name):
    print("Searching...")
    with open("library.txt") as file:
        for line in file:
            print(f"Looked in location: {line.strip()} ")
    print("...Done!")


def run():
    import os
    path = os.getcwd()
    search(path)


if __name__ == "__main__":
    run()
