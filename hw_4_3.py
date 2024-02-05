# Модуль 4. Завдання 3

import sys, os
from pathlib import Path

# from colorama import Fore, Back, Style


def main():
    os.system("cls")

    # print_dir("salary_file.txt")
    print_dir("books")
    # print_dir("D:\Books\Stephen King")


def print_dir(path, indent=0):
    path = Path(path)
    if path.exists():

        if path.is_dir():
            if indent == 0:
                print(f"📦 {path}")  # Задати потрібний колір
            else:
                print(f"{' '*indent}📂 {path.name}")  # Задати потрібний колір
            for path in path.iterdir():
                print_dir(path, indent + 2)
        else:
            print(f"{' '*indent}📜 {path.name}")  # Задати потрібний колір


if __name__ == "__main__":
    main()
