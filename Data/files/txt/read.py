import os


def display_chars(path,num_char):

    with open("library.txt") as file:
        partial_data = file.read(num_char)
    return partial_data


def display_line(path):
    with open("library.txt") as file:
        line = file.readline()
    return line


def display_text(path):
    with open("library.txt") as file:
        data = file.read()
    return data


def run():
    import os
    path = os.getcwd()
    print("How many characters do you want to read?")
    num_char = int(input())
    print(f"The first {num_char} characters are:")
    print(display_chars(path, num_char))
    print()
    print("The first line is:")
    print(display_line(path))
    print()
    print("The full text is:")
    print(display_text(path))


if __name__ == "__main__":
    run()
