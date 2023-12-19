# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку.
# Другий потік знаходить середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

import threading

user_input = input("Введіть значення у список (розділіть числа пробілами): ")
numbers = [float(x) for x in user_input.split()]

# Функція для знаходження суми елементів у списку
def find_summ(numbers):
    global summ_result
    summ_result = sum(numbers)

# Функція для знаходження середнього арифметичного у списку
def find_aryfmet(numbers):
    global aryfmet_result
    aryfmet_result = sum(numbers) / len(numbers)

# Створення потоків
summ_thread = threading.Thread(target=find_summ, args=(numbers,))
aryfmet_thread = threading.Thread(target=find_aryfmet, args=(numbers,))

summ_thread.start()
aryfmet_thread.start()
summ_thread.join()
aryfmet_thread.join()

print("Сума елементів у списку:", summ_result)
print("Середнє арифметичне у списку:", aryfmet_result)
