book_information= [
    {
        "Title": "To Kill a Mockingbird",
        "Author": "Harper Lee",
        "Year of Publication": 1960,
        "ISBN": "9780061120084",
        "Available": True
    },
    {
        "Title": "1984",
        "Author": "George Orwell",
        "Year of Publication": 1949,
        "ISBN": "9780451524935",
        "Available": True
    },
    {
        "Title": "The Great Gatsby",
        "Author": "F. Scott Fitzgerald",
        "Year of Publication": 1925,
        "ISBN": "9780743273565",
        "Available": True
    }
]


def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of publication: "))
    isbn = input("Enter the ISBN of the book: ")
    available = True

    new_book = {
        "Title": title,
        "Author": author,
        "Year of Publication": year,
        "ISBN": isbn,
        "Available": available
    }

    book_information.append(new_book)
    print(f"Book added successfully!")
    print()


def view_books():
    if not book_information:
        print("No books in the library.")

    for index, book in enumerate(book_information, start=1):
        print(f"Book {index}:")
        print(f"  Title       : {book["Title"]}")
        print(f"  Author      : {book["Author"]}")
        print(f"  Year        : {book["Year of Publication"]}")
        print(f"  ISBN        : {book["ISBN"]}")
        print(f"  Available   : {True if book["Available"] else False}")
        print()


def update_book():
    while True:
        user_isbn = int(input("Enter the ISBN of the book to update (or type '0' to cancel): "))
        if user_isbn == "0":
            print("Exiting the update process.")
            break
        
        for book in book_information:
            if user_isbn == book["ISBN"]:
                print("book details:")
                print(f"  Title       : {book['Title']}")
                print(f"  Author      : {book['Author']}")
                print(f"  Year        : {book['Year of Publication']}")
                print(f"  ISBN        : {book['ISBN']}")
                print(f"  Available   : {True if book['Available'] else False}")
                print()
                
                book['Title'] = input("Enter the new title (or press Enter to keep current): ") or book['Title'].lower()
                book['Author'] = input("Enter the new author (or press Enter to keep current): ") or book['Author'].lower()
                book['Year of Publication'] = int(input("Enter the new year (or press Enter to keep current): ") or book['Year of Publication'])
                book['Available'] = input("Is the book available? (yes/no): ").strip().lower() == 'yes'
                print("Book details updated successfully!")
                print()

                print("updated book details:")
                print(f"  Title       : {book['Title']}")
                print(f"  Author      : {book['Author']}")
                print(f"  Year        : {book['Year of Publication']}")
                print(f"  ISBN        : {book['ISBN']}")
                print(f"  Available   : {True if book['Available'] else False}")
                break
        
        if user_isbn != book["ISBN"]:
            print("ISBN not found! Please enter a valid ISBN.")
        else:
            break



def delete_book():
    while True:
        delete_isbn = int(input("Enter the ISBN of the book to delete (or type '0' to cancel): "))
        if delete_isbn == "0":
            print("Exiting the delete process.")
            break
        
        for book in book_information:
            if delete_isbn == book["ISBN"]:
                book_information.remove(book)
            print("Book deleted successfully")
            print()
            break
            
        else:
            if delete_isbn != book["ISBN"]:
                print("ISBN not found! Please enter a valid ISBN.")
                print()
                continue
        break


def search_book():
    while True:
        search_title = (input("Enter the title of the book to search (or type '0' to cancel): "))
        if search_title == "0":
            print("Exiting the search process.")
            break
        
        for book in book_information:
            if search_title == book["Title"]:
                print("book found!!")
                print()
                print("book details:")
                print(f"  Title       : {book['Title']}")
                print(f"  Author      : {book['Author']}")
                print(f"  Year        : {book['Year of Publication']}")
                print(f"  ISBN        : {book['ISBN']}")
                print(f"  Available   : {True if book['Available'] else False}")
                print()
                break
            
        else:
            if search_title != book["Title"]:
                print("Book title not found! Please enter a valid book title .")
                print()
                continue
        break


def borrow_book():
    print("These are all the available books you can borrow:")
    available_books = [book for book in book_information if book["Available"]]

    if not available_books:
        print("No books are currently available for borrowing.")
        return

    for index, book in enumerate(available_books, start=1):
        print(f"Book {index}:")
        print(f"  Title       : {book['Title']}")
        print(f"  Author      : {book['Author']}")
        print(f"  Year        : {book['Year of Publication']}")
        print(f"  ISBN        : {book['ISBN']}")
        print(f"  Available   : {True if book['Available'] else False}")
        print()

    user_borrow = input("Enter the title of the book to borrow (or type '0' to cancel): ")
    if user_borrow == "0":
        print("Borrowing process canceled.")
        return

    for book in available_books:
        if user_borrow == book["Title"]:
            book["Available"] = False
            print(f"You have successfully borrowed '{book['Title']}'.")
            return

    print("Book title not found! Please enter a valid book title.")



def return_book():
    user_return = input("Enter the title of the book to return (or type '0' to cancel): ")
    if user_return == "0":
        print("Returning process canceled.")
        return

    for book in book_information:
        if user_return == book["Title"]:
            if book["Available"]:
                print(f"'{book['Title']}' is already available in the library.")
                return
            else:
                book["Available"] = True
                print(f"You have successfully returned '{book['Title']}'.")
                return

    print("Book title not found! Please enter a valid book title.")


def menu():
    while True:
        print(""" Welcome to the Digital Library System
        Select operation you want to perform:
        1. Add Books 
        2. View Books
        3. Update Books
        4. Delete Book
        5. Search Books
        6. Borrow Books
        7. Return Books
        8. Exit""")
        
        user_choice = input("Enter your choice in number using the number (1-8): ")
        print()

        if user_choice == "8":
            print("You chose to exit!!!")
            print("Exiting the Library. Goodbye!")
            break

        elif user_choice == "1":
            print("You chose to Add books!!!")
            print()
            add_book()

        elif user_choice == "2":
            print("You chose to view books!!!")
            print()
            view_books()

        elif user_choice == "3":
            print("You chose to update book!!!")
            print()
            update_book()

        elif user_choice == "4":
            print("You chose to delete books!!!")
            print()
            delete_book()

        elif user_choice == "5":
            print("You chose to search books!!!")
            print()
            search_book()

        elif user_choice == "6":
            print("You chose to borrow books!!!")
            print()
            borrow_book()

        elif user_choice == "7":
            print("You chose to return books!!!")
            print()
            return_book()
        

        else:
            print("Invalid choice. Please select a valid option from 1 - 8")
            continue

menu()
            