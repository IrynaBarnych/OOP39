# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

import threading

file_path = input("Введіть шлях до файлу: ")
search_word = input("Введіть слово для пошуку: ")

with open(file_path, "r") as file:
    content = file.read()

# Функція для пошуку слова у файлі
def find_word(content, search_word):
    count_occurrences = content.count(search_word)
    return count_occurrences


search_thread = threading.Thread(target=find_word, args=(content, search_word))

search_thread.start()

search_thread.join()

result = find_word(content, search_word)
print(f"Слово '{search_word}' зустрічається у файлі {result} разів.")