def search(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open("books.txt") as file:
        for line in file:
            if file.read(7) == "Section":
                sections = f"{line}\n"
            else:
                books = f"{line}\n"
    print("...Done!")
    final = f"{sections}\n\n{books}"
    return final

def save(path,data):
    print("Saving...")




