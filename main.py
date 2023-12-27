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

number_list = []
lock = threading.Lock()
list_filled_event = threading.Event()

def fill_list():
    global number_list
    with lock:
        number_list = [random.randint(1, 100) for _ in range(10)]
    list_filled_event.set()

def calculate_sum():
    global number_list
    with lock:
        return sum(number_list)

def calculate_average():
    global number_list
    with lock:
        return sum(number_list) / len(number_list)

fill_thread = threading.Thread(target=fill_list)
fill_thread.start()

list_filled_event.wait()

sum_result = calculate_sum()
average_result = calculate_average()

print("Згенерований список:", number_list)
print("Сума елементів у списку:", sum_result)
print("Середнє арифметичне значення у списку:", average_result)

