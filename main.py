# Завдання 2
# Користувач вводить з клавіатури шлях до файлу. Після
# чого запускаються три потоки. Перший потік заповнює файл
# випадковими числами. Два інші потоки очікують на заповнення.
# Коли файл заповнений, обидва потоки стартують.
# Перший потік знаходить усі прості числа,
# другий потік знаходить факторіал кожного числа у файлі.
# Результати пошуку
# кожен потік має записати у новий файл. Виведіть на екран
# статистику виконаних операцій.

import threading
import random
import math

NUMBERS_COUNT = 10

count_even_numbers = 0
count_odd_numbers = 0
count_primes = 0
factorials = []

file_path = input("Введіть шлях до файлу: ")

def generate_random_numbers(file_name):
    random_numbers = [str(random.randint(1, 10)) + "\n" for _ in range(NUMBERS_COUNT)]
    with open(file_name, "w") as file:
        file.writelines(random_numbers)

def find_primes(numbers, file_name):
    global count_primes
    primes = [str(num) + "\n" for num in numbers if is_prime(num)]
    count_primes = len(primes)
    with open(file_name, "w") as file:
        file.writelines(primes)

def calculate_factorials(numbers, file_name):
    global factorials
    factorials = [str(math.factorial(num)) + "\n" for num in numbers]
    with open(file_name, "w") as file:
        file.writelines(factorials)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

generate_thread = threading.Thread(target=generate_random_numbers, args=(file_path,))
primes_thread = threading.Thread(target=find_primes, args=(range(1, NUMBERS_COUNT + 1), "primes.txt"))
factorials_thread = threading.Thread(target=calculate_factorials, args=(range(1, NUMBERS_COUNT + 1), "factorials.txt"))

generate_thread.start()
generate_thread.join()

primes_thread.start()
factorials_thread.start()

primes_thread.join()
factorials_thread.join()

print("Кількість простих чисел: ", count_primes)
print("Факторіали чисел збережені у файлі 'factorials.txt'")





