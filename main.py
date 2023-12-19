# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading

user_input = input("Введіть значення у список (розділіть числа пробілами): ")
numbers = [int(x) for x in user_input.split()]

# Функція для знаходження максимуму у списку
def find_max(numbers):
    global max_result
    max_result = max(numbers)

# Функція для знаходження мінімуму у списку
def find_min(numbers):
    global min_result
    min_result = min(numbers)

# Створення потоків
max_thread = threading.Thread(target=find_max, args=(numbers,))
min_thread = threading.Thread(target=find_min, args=(numbers,))

max_thread.start()
min_thread.start()
max_thread.join()
min_thread.join()

print("Максимум у списку:", max_result)
print("Мінімум у списку:", min_result)
