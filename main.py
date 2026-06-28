import os

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        os.system("python add_book.py")

    elif choice == "2":
        os.system("python view_books.py")

    elif choice == "3":
        os.system("python issue_book.py")

    elif choice == "4":
        os.system("python return_book.py")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")