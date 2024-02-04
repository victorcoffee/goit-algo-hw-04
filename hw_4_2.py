# Модуль 4. Завдання 2

import os
from pathlib import Path

# Функція повертає список словників з інформацією про кожного кота.
# Дані беруться з вказаного файлу

def get_cats_info(path):
    cats_info = []
    file_path = Path(path)
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            try:
                cat_info = {}
                id, name, age = line.split(",")
                cat_info["id"] = id
                cat_info["name"] = name
                cat_info["age"] = age.strip()
                cats_info.append(cat_info)
            except:
                # Якщо дані в рядку некоректні - відсутні коми, зайві коми
                # cat_info["id"] = None
                # cat_info["name"] = None
                # cat_info["age"] = None
                print(f"Помилка в рядку: {line.strip()}")
                # pass

        return cats_info
    else:
        print(f"Файл {file_path} не існує")
    return cats_info


# Основна програма

os.system("cls")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
