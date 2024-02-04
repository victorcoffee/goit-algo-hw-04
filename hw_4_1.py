# Модуль 4. Завдання 1


def total_salary(path):
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

# Основна програма

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
