# Завдання 4
# Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
# потоки. Перший потік має знайти файли з потрібним словом
# і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
# заборонених слів (список цих слів потрібно зчитати з файлу
# із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.

import threading
import os

def find_and_merge_files(directory, search_word, merged_file_path):
    files_with_word = []

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                if search_word in content:
                    files_with_word.append(filepath)

    merged_content = ""
    for file_path in files_with_word:
        with open(file_path, 'r') as file:
            merged_content += file.read()

    with open(merged_file_path, 'w') as merged_file:
        merged_file.write(merged_content)

def exclude_forbidden_words(input_file_path, forbidden_words_file, output_file_path):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    with open(forbidden_words_file, 'r') as forbidden_file:
        forbidden_words = forbidden_file.read().split()

    for word in forbidden_words:
        content = content.replace(word, '')

    with open(output_file_path, 'w') as output_file:
        output_file.write(content)

directory_path = input("Введіть шлях до директорії: ")
search_word = input("Введіть слово для пошуку: ")

forbidden_words_file_path = input("Введіть повний шлях до файлу з забороненими словами ('forbidden_words.txt'): ")

merged_file_path = 'merged_content.txt'
output_file_path = 'output_content.txt'

merge_thread = threading.Thread(target=find_and_merge_files, args=(directory_path, search_word, merged_file_path))
exclude_thread = threading.Thread(target=exclude_forbidden_words,
                                  args=(merged_file_path, forbidden_words_file_path, output_file_path))

merge_thread.start()
merge_thread.join()
exclude_thread.start()
exclude_thread.join()

print("Операції завершено.")
