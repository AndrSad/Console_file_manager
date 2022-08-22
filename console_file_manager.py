
"""
УРОК 7, ЗАДАНИЕ 2
5. В программе консольный файловый менеджер есть пункт "просмотр содержимого рабочей директории";

6. Добавить пункт "сохранить содержимое рабочей директории в файл";

7. При выборе этого пункта создать файл listdir.txt (если он есть то пересоздать)
и сохранить туда содержимое рабочей директории следующим образом: сначала все файлы,
потом все папки, пример как может выглядеть итоговый файл.

files: victory.py, bill.py, main.py
dirs: modules, packages
"""

import os
import shutil


while True:
    print('1. Просмотр содержимого рабочей директории')
    print('2. Сохранить содержимое рабочей директории в файл')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        files = list(filter(os.path.isfile, os.listdir()))
        dirs = list(filter(os.path.isdir, os.listdir()))
        print(files, type(files))
        print(dirs, type(dirs))
        print()
    elif choise == '2':
        with open('listdir.txt', 'w') as f:
            f.write('Files: ')
            for file in files:
                f.write(f'{file}, ')
            f.write('\n')
            f.write('Dirs: ')
            for dir in dirs:
                f.write(f'{dir}, ')
        break
    elif choise == '3':
        break
    else:
        print('Неправильно введены данные')





