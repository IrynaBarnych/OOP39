# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
"""Користувач вводить з клавіатури шлях до файлу, що
містить набір чисел. Після чого запускаються два потоки.
Перший потік створює новий файл, в який запише лише
парні елементи списку. Другий потік створює новий файл,
в який запише лише непарні елементи списку. Кількість
парних і непарних елементів виводиться на екран.
"""
import threading
count_even_numbers = 0
count_odd_numbers = 0
#отримання шлях від користувачя
file_path = input("Введіть шлях до файлу: ")
#зчитуємо файл
with open(file_path, "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]
#функція для запису парних чисел
def write_even_numbers(numbers, file_name):
    even_numbers = [str(num) + "\n" for num in numbers if not num & 1]
    global count_even_numbers
    count_even_numbers = len(even_numbers)
    with open(file_name, "w") as file:
        file.writelines(even_numbers)
    return len(even_numbers)

#функція для запису непарних чисел
def write_odd_numbers(numbers, file_name):
    odd_numbers = [str(num) + "\n" for num in numbers if num & 1]
    global count_odd_numbers
    count_odd_numbers = len(odd_numbers)
    with open(file_name, "w") as file:
        file.writelines(odd_numbers)
    return len(odd_numbers)

#створення потоків
even_thread = threading.Thread(target=write_even_numbers, args=(numbers, "even_numbers.txt"))
odd_thread = threading.Thread(target=write_odd_numbers, args=(numbers, "odd_numbers.txt"))

even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()

print("Кількість парних чисел ", count_even_numbers)
print("Кількість непарних чисел ", count_odd_numbers)