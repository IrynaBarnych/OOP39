# Завдання 1
# При старті додатку запускаються три потоки. Перший
# потік заповнює список випадковими числами. Два інші потоки
# очікують на заповнення. Коли перелік заповнений, обидва
# потоки запускаються. Перший потік знаходить суму елементів
# списку, другий потік знаходить середнє арифметичне значення
# у списку. Отриманий список, сума та середнє арифметичне
# виводяться на екран.

import threading
import random

user_input = input("Введіть значення у список (розділіть числа пробілами): ")
numbers = [int(x) for x in user_input.split()]

list_filled_event = threading.Event()
number_list = []
sum_result = None
average_result = None

def fill_list():
    global number_list
    with list_filled_event.get_lock():
        number_list = [random.randint(1, 100) for _ in range(10)]
    list_filled_event.set()

def calculate_sum():
    global sum_result, number_list
    with list_filled_event.get_lock():
        sum_result = sum(number_list)

def calculate_average():
    global average_result, number_list
    with list_filled_event.get_lock():
        average_result = sum(number_list) / len(number_list)

fill_thread = threading.Thread(target=fill_list)
sum_thread = threading.Thread(target=calculate_sum)
average_thread = threading.Thread(target=calculate_average)

fill_thread.start()

list_filled_event.wait()

sum_thread.start()
average_thread.start()

fill_thread.join()
sum_thread.join()
average_thread.join()

print("Введений список:", numbers)
print("Згенерований список:", number_list)
print("Сума елементів у списку:", sum_result)
print("Середнє арифметичне значення у списку:", average_result)



