import create_contact_file
import view_all_contacts_file


contact_book = []


def search_contacts():
    search_term = input("Enter what you want to search: ")
    for contact in contact_book:

        search_term_lowercase = search_term.lower()
        name_lowercase = contact["name"].lower()

        if search_term_lowercase in name_lowercase:
            print(f"Found: {contact['name']} - {contact['phone']}")


def remove_contact():
    # search -> select -> delete
    search_term = input("Enter text to search to remove: ")
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact["name"].lower():
            print(f"{index+1}. {contact['name']} - {contact['phone']}")
    selected_index = input("Enter an contact to remove:")
    selected_index = int(selected_index)

    contact_book.pop(selected_index - 1)

    print("Contact removed succesfully.")


def update_contact():
    # 1. Select the contact
    found_search_result = False

    search_term = input("Enter text to search to update: ")
    for index, contact in enumerate(contact_book):
        if search_term.lower() in contact["name"].lower():
            found_search_result = True
            print(f"{index+1}. {contact['name']} - {contact['phone']}")

    if not found_search_result:
        print("No item found")
        return

    selected_index = input("Enter an contact to update:")
    selected_index = int(selected_index)

    # - #
    # If user wants to update specific field
    # Take name of the field as input
    # Update only those value

    # 2. Get new values
    new_name = input("Enter New Name: ")
    new_phone = input("Enter New Phone: ")
    new_email = input("Enter New Email: ")

    # 3. Replace the old values with new values

    # Method 1
    # contact_book[selected_index - 1]["name"] = new_name
    # contact_book[selected_index - 1]["phone"] = new_phone
    # contact_book[selected_index - 1]["email"] = new_email

    # Method 2
    contact_book[selected_index - 1].update(
        {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
        }
    )

    print("Contact updated successfully!")


def backup_contact():
    # take all the contact and write them to a file
    # name,phone,email

    # file_pointer = open("contacts.csv", "wt")

    with open("contacts.csv", "wt") as file_pointer:
        for contact in contact_book:
            line = f"{contact['name']},{contact['phone']},{contact['email']}\n"
            file_pointer.write(line)

    # file_pointer.close()

    print("Contacts Backed Up!")


def restore_contact():
    # open file
    # read all contacts
    # save them to global contact book variable

    contact_book.clear()

    with open("contacts.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            contact = {
                "name": line_splitted[0],
                "phone": line_splitted[1],
                "email": line_splitted[2],
            }
            contact_book.append(contact)

    print("Contacts Restored!")


print("Welcome!")

menu_text = """
Your options:
1. Create Contact
2. View All Contacts
3. Search Contacts
4. Remove Contact
5. Update Contact
6. Backup Contact
7. Restore Contact
0. Exit
"""

while True:
    print(menu_text)
    choice = input("Enter your choice: ")

    if choice == "1":
        contact_book = create_contact_file.create_contact(contact_book)
    elif choice == "2":
        view_all_contacts_file.view_all_contacts(contact_book)
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        backup_contact()
    elif choice == "7":
        restore_contact()
    elif choice == "0":
        print("Thanks for using the application.")
        break
    else:
        print("Wrong Choice!")
