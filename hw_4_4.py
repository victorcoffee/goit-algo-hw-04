# Модуль 4. Завдання 4

import os
from pathlib import Path


# Парсер команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Додавання контакту
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Зміна контакту
def change_contact(args, contacts):
    name, phone = args
    contacts.update({name: phone})
    return "Contact updated."


# Пошук номера телефону контакту
def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)

    # Якщо контакт існує
    if phone:
        return phone
    else:
        return "This name is not in your Contacts."


#  Виведення всіх контаків
def show_all(contacts):
    print(*contacts)
    for name, phone in contacts.items():
        print(f"{name} {phone}")

    return "All list of contacts printed."

# Основна програма
def main():
    os.system("cls")
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
