#HW4 task4
import os
from colorama import Fore, Back, Style

#handler funcions
#function to parse input from user
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() 
    return cmd, *args

#function to add a contact in a dictionary
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

#function to change a phone number by a name
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed"
    else:
        return "There is no contact with requested name"

#function to show phone number by a name    
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone of {name} is {contacts[name]}"
    else:
        return "Phone is not in contacts"    

#function to show all contacts
def show_all(contacts):
    if len(contacts) == 0:
        return "Contacts are empty"
    for key in contacts:
        print(f"Name: {key.capitalize()}, phone: {contacts[key]}")
    return "End of show all command"
#main logic
def main():
    print("Welcome to the assistant bot")

    contacts = {}
    
    while True:
        user_input = input(Fore.MAGENTA + "Enter a command:\n" + Style.RESET_ALL).strip().lower()
        Style.RESET_ALL

        command, *args = parse_input(user_input)

        if command == 'exit' or command == 'close':
            print("Good bye!")
            os._exit(0)

        elif command == 'hello':
            print('How can I help you?')
            continue

        elif command == 'add':
            print("=== Add contact start ===")
            print(add_contact(args, contacts))
            print("=== Add contact end ===")

        elif command == 'change':
            print("=== Change contact start ===")
            change_contact(args, contacts)
            print("=== Change contact end ===")

        elif command == 'phone':
            print("=== Show phone start ===")
            print(show_phone(args, contacts))  
            print("=== Show phone end ===")

        elif command == 'all':
            print("=== Show all contacts start ===")
            print(show_all(contacts))
            print("=== Show all contacts end ===")
        else:
            print("Invalid command. Please correct your input.")

    print("End of contact assistant work")


if __name__ == "__main__":
    main()