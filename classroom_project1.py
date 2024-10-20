import sys

def show_memory_usage(data_structure):
    return sys.getsizeof(data_structure)

def add_contact(contacts_book, name, phone, email):
    contacts_book.append((name, phone, email))
    print(f"Added {name}. Memory usage: {show_memory_usage(contacts_book)} bytes")

def remove_contact(contacts_book, name):
    removed = [contact for contact in contacts_book if contact[0] == name]
    if removed:
        contacts_book[:] = [contact for contact in contacts_book if contact[0] != name]
        print(f"Removed {name}. Memory usage: {show_memory_usage(contacts_book)} bytes")
    else:
        print(f"No contact found with the name {name}.")

def search_contact(contacts_book, name):
    found = [contact for contact in contacts_book if contact[0] == name]
    return found

def main():
    contacts_book = []
    add_contact(contacts_book, 'Alik', '123-456-7890', 'alik@magti.com')
    add_contact(contacts_book, 'Bidzina', '234-567-8901', 'bidzina@mail.ru')


    print("Welcome to the Contacts System.")
    while True:
        user_input = input(
            "Please enter one of the following commands: \n"
            "1. Add Contact\n"
            "2. Remove Contact\n"
            "3. Search Contact \n"
            "4. Get Memory Used by Contacts \n")

        match user_input:
            case "1":
                print("adding the contact…")
                while True:
                    input_name=input("Please input the name of the contact: ").capitalize().strip()
                    input_phone=input("Enter the phone number: ").strip()
                    input_email=input("Enter email address: ").strip()
                    valid_email='@' in input_email and ('.' in input_email)  #martivi email validacia
                    if input_name.isalpha() and input_phone.isnumeric() and valid_email: #saerTo validacia
                        add_contact(contacts_book, input_name, input_phone, input_email)
                        break
                    else: "Incorrect data entry, try again..."
            case "2":
                print("removing the contact…")
                remove_name=input("Please input the name of the contact to remove: ").capitalize().strip()
                remove_contact(contacts_book, remove_name)


            case "3":
                print("search for the contact…")
                while True:
                    input_name = input("Please input the name of the contact to look for: ").capitalize().strip()

                    found = search_contact(contacts_book, input_name)
                    if found:
                        for contact in found:
                            print(f"Found: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
                    else:
                        print(f"No contact found with the name {input_name}.")
                    break
            case "4":
                print(f"Memory usage: {show_memory_usage(contacts_book)}")

            case _:
                print("Incorrect operation - please enter the number between 1 and 3")




main()