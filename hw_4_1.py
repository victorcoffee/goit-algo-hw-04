# Модуль 4. Завдання 1
import os
from pathlib import Path

# Функція підраховує сумарну і середню зарплату за даними зі вказаного файла

def total_salary(path):
    path_file = Path(path)
    if path_file.exists():
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        total = 0
        count = 0
        for line in lines:
            (_, salary) = line.split(",")
            salary = float(salary)
            total += salary
            count += 1

        if count > 0:
            average = total / count
        else:
            average = 0

        return (total, average)
    else:
        print(f"Файл {path_file} не існує")
        return (None, None)


# Основна програма
os.system("cls")

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
