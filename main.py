# Завдання 3
# Користувач вводить з клавіатури шлях до існуючої та
# до нової директорії. Після чого запускається потік, який має
# скопіювати вміст директорії у нове місце. Збережіть структуру
# директорії. Виведіть статистику виконаних операцій на екран.

import threading
import shutil
import os

def copy_directory(source_path, destination_path):
    try:

        shutil.copytree(source_path, destination_path)
        return True
    except Exception as e:
        print(f"Помилка копіювання: {e}")
        return False

def count_files_and_subdirectories(directory):
    files = 0
    subdirectories = 0
    for _, dirs, filenames in os.walk(directory):
        subdirectories += len(dirs)
        files += len(filenames)
    return files, subdirectories


source_directory = input("Введіть шлях до існуючої директорії: ")
destination_directory = input("Введіть шлях до нової директорії: ")

copy_thread = threading.Thread(target=copy_directory, args=(source_directory, destination_directory))

copy_thread.start()
copy_thread.join()

if os.path.exists(destination_directory):
    files, subdirectories = count_files_and_subdirectories(destination_directory)
    print(f"Кількість скопійованих файлів: {files}")
    print(f"Кількість скопійованих піддиректорій: {subdirectories}")
else:
    print("Копіювання не вдалося.")
