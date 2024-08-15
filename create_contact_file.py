def create_contact(contact_book):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
    }

    contact_book.append(contact)

    # Open contacts.csv here in append mode - "a"
    # write(contact)

    print("Contact created successfully!")
    return contact_book
