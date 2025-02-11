contact_information = [
    {
        "Name": "Adewale",
        "Phone Number": "09042546784",
        "Favourite": True
    },
    {
        "Name": "Israel",
        "Phone Number": "09085769475",
        "Favourite": True
    },
        {
        "Name": "Jesu",
        "Phone Number": "08154675897",
        "Favourite": True
    }
]


def add_contact():
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number: ")
    favourite = input("do you wan to add to Favourite: (Yes or No)? ")

    new_contact = {
        "Name": name,
        "Phone Number": phone_number,
        "Favourite": favourite
    }

    contact_information.append(new_contact)
    if favourite == "yes":
        contact_information["Favourite"] = True
    else:
        contact_information["Favourite"] = False

    print(f"contact added successfully!")
    print()


def view_contact():
    if not contact_information:
        print("No contact in the library.")

    for index, contact in enumerate(contact_information, start=1):
        print(f" Contact {index}:")
        print(f"  Name       :    {contact["Name"]}")
        print(f"  Phone Number  : {contact["Phone Number"]}")
        print(f"  Favourite   :   {contact["Favourite"]}")
        print()


def update_contact():
    while True:
        user_contact_info = input("Enter the Phone Number to update (or type '0' to cancel): ")
        if user_contact_info == "0":
            print("Exiting the update process.")
            break
        
        for contact in contact_information:
            if user_contact_info == contact["Phone Number"]:
                print("Contact details:")
                print(f"  Name       : {contact['Name']}")
                print(f"  Phone Number : {contact['Phone Number']}")
                print(f"  Favourite   : {contact['Favourite']}")
                print()
                
                contact["Name"] = input("Enter the new name (or press Enter to keep current): ") or contact["Name"]
                contact["Phone Number"] = input("Enter the new phone number (or press Enter to keep current): ") or contact["Phone Number"]
                favourite_input = input("Mark as favourite (True/False) (or press Enter to keep current): ")
                if favourite_input.lower() == "true":
                    contact["Favourite"] = True
                elif favourite_input.lower() == "false":
                    contact["Favourite"] = False

                print("Contact details updated successfully!")
                print()

                print("Updated contact details:")
                print(f"  Name       : {contact['Name']}")
                print(f"  Phone Number : {contact['Phone Number']}")
                print(f"  Favourite    : {contact['Favourite']}")
                break
        
        else:
            print("Phone number not found! Please enter a valid phone number.")
        
        break



def delete_contact():
    while True:
        delete_user_contact = input("Enter the Phone Number to delete (or type '0' to cancel): ")
        
        if delete_user_contact == "0":
            print("Exiting the delete process.")
            break

        for contact in contact_information:
            if delete_user_contact == contact["Phone Number"]:
                contact_information.remove(contact)
                print("Contact deleted successfully.")
                print()
                break
        else:
            print("Phone Number not found! Please enter a valid Phone Number.")
            print()
            continue

        break



def search_contact():
    while True:
        search_title = (input("Enter the Name to search the contact (or type '0' to cancel): "))
        if search_title == "0":
            print("Exiting the search process.")
            break
        
        for contact in contact_information:
            if search_title == contact["Name"]:
                print("contact found!!")
                print()
                print("contact details:")
                print(f"  Name       :    {contact["Name"]}")
                print(f"  Phone Number  : {contact["Author"]}")
                print(f"  Available   :   {contact["Favourite"]}")
                print()
                break
            
        else:
            if search_title != contact["Name"]:
                print("Book title not found! Please enter a valid book title .")
                print()
                continue
        break


def mark_favourite():
    user_favourite = input("Enter the phone number to mark as favourite (or type '0' to cancel): ")

    if user_favourite == "0":
        print("Operation canceled.")
        return

    for contact in contact_information:
        if user_favourite == contact["Phone Number"]:
            if contact["Favourite"]:
                print(f"{contact['Name']} is already marked as favourite.")
            else:
                contact["Favourite"] = True
                print(f"{contact['Name']} has been marked as favourite.")
                print()
            return

    print("Contact not found! Please enter a valid phone number.")



def unmark_favourite():
    user_unfavourite = input("Enter the phone number to mark as favourite (or type '0' to cancel): ")

    if user_unfavourite == "0":
        print("Operation canceled.")
        return

    for contact in contact_information:
        if user_unfavourite == contact["Phone Number"]:
            if not contact["Favourite"]:
                print(f"{contact['Name']} is already marked as favourite.")
            else:
                contact["Favourite"] = False
                print(f"{contact['Name']} has been unmarked as favourite.")
                print()
            return

    print("Contact not found! Please enter a valid phone number.")



def menu():
    while True:
        print(""" Welcome to the Digital Library System
        Select operation you want to perform:
        1. Add contact 
        2. View contact
        3. Update contact
        4. Delete contact
        5. Search contact
        6. Mark contact as favourite
        7. Unmark contact as favourite
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
            add_contact()

        elif user_choice == "2":
            print("You chose to view contact!!!")
            print()
            view_contact()

        elif user_choice == "3":
            print("You chose to update contact!!!")
            print()
            update_contact()

        elif user_choice == "4":
            print("You chose to delete contact!!!")
            print()
            delete_contact()

        elif user_choice == "5":
            print("You chose to search contact!!!")
            print()
            search_contact()

        elif user_choice == "6":
            print("You chose to mark contact favourite!!!")
            print()
            mark_favourite()

        elif user_choice == "7":
            print("You chose to unmark contact as favourite!!!")
            print()
            unmark_favourite()
        

        else:
            print("Invalid choice. Please select a valid option from 1 - 8")
            continue

menu()
            