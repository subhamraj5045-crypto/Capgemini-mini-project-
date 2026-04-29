library = []

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!")

def view_books():
    if len(library) == 0:
        print("No books in library")
    else:
        print("Books in library:")
        for b in library:
            print("-", b)

def remove_book():
    book = input("Enter book name to remove: ")
    if book in library:
        library.remove(book)
        print("Book removed!")
    else:
        print("Book not found!")
