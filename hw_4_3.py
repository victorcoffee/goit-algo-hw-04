# Не встигаю завершити завдання 3, яке помічене як необов'язкове.
# Але маю намір зробити його.
# Чи можна доздати його пізніше?

# Модуль 4. Завдання 3

import sys, os
from pathlib import Path


def main():
    os.system("cls")
    
    # Рядок для запуску: python hw_4_3.py salary_file.txt
    # Рядок для запуску: python hw_4_3.py books
    # print_dir(".venv")
    # print_dir("salary_file.txt")
    
    print_dir("books")


def print_dir(path, indent=0):
    base_path = Path(path)
    if base_path.exists():

        if base_path.is_dir():
            if indent == 0:
                print(f"📦 {base_path}")  # Задати потрібний колір
            else:
                print(f"{' '*indent}📂 {base_path}")  # Задати потрібний колір
            for path in base_path.iterdir():
                print_dir(path, indent + 1)
        else:
            print(f"{' '*indent}📜 {base_path}")  # Задати потрібний колір


if __name__ == "__main__":
    main()
