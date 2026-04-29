from library.operations import add_book, view_books, remove_book

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
