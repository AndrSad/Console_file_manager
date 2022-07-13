
import os
import platform
import shutil


def information_system():
    # информация о системе
    print('----------')
    print()
    print(platform.system(), platform.release(), platform.win32_edition(), platform.architecture())
    print()
    print('----------')
# print(platform.win32_ver())
# print(platform.platform())
# print()
# print(platform.machine())
# print(platform.node())
# print(platform.processor())
# print(platform.python_build())


def mk_dir():
    # Создать пустой каталог (папку)
    print('----------')
    print()
    folder_name = input('Введите название создаваемой папки: ')
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    else:
        print("Папка с таким именем уже существует.")
    print()
    print('----------')


def ch_dir():
    # Изменение директории. Изменение текущего каталога
    print('----------')
    print()
    print("Текущая директория:", os.getcwd())
    new_dir = input("Введите название директории для перехода глубже, либо .. для перехода выше: ")
    os.chdir(new_dir)
    print("Измененная текущая директория: ", os.getcwd())
    print()
    print('----------')


def list_dir():
    # Список файлов и директорий. Распечатать все файлы и папки в текущем каталоге
    print('----------')
    print()
    print("Все папки и файлы:", os.listdir())
    print()
    print('----------')


def dir_names():
    # распечатать все вложенные папки
    print('----------')
    print()
    for dirpath, dirnames, filenames in os.walk("."): # это генератор дерева каталогов.
                                                      # Он будет перебирать все переданные составляющие.
                                                      # Здесь в качестве аргумента передано значение «.»,
                                                      # которое обозначает верхушку дерева
        # перебрать каталоги
        for dirname in dirnames:
            print("Папки:", os.path.join(dirpath, dirname)) # Метод os.path.join() использован для
                                                            # объединения текущего пути с именем файла/папки.
    print()
    print('----------')


def file_names():
    # распечатать все вложенные файлы
    print('----------')
    print()
    for dirpath, dirnames, filenames in os.walk("."):  # это генератор дерева каталогов.
                                                       # Он будет перебирать все переданные составляющие.
                                                       # Здесь в качестве аргумента передано значение «.»,
                                                       # которое обозначает верхушку дерева
        # перебрать файлы
        for filename in filenames:
            print("Файлы:", os.path.join(dirpath, filename))
    print()
    print('----------')


def rm_dir():
    # Удаление директории/папки
    print('----------')
    print()
    folder_name = input('Введите название удаляемой папки: ')
    if os.path.isdir(folder_name):
        os.rmdir(folder_name)
    else:
        print("Папки с таким именем не существует.")
    print()
    print('----------')


def copy_file():
    # Копирование файла
    print('----------')
    print()
    old_file = input("Введите имя копируемого файла: ")
    new_file = input("Введите имя нового файла: ")
    shutil.copyfile(old_file, new_file)
    print()
    print('----------')


def my_info():
    # Информация о создателе программы
    f = open('my_info.txt', 'r')
    print('----------')
    print()
    print(*f)
    print()
    print('----------')


# Создание вложенных папок
# Создать несколько вложенных друг в друга папок
# os.makedirs("nested1/nested2/nested3")

# Создание файлов
# Создать новый текстовый файл
# text_file - open("text.txt", "w") # Открытие заданного файла на компьютере, если его нет, то создается данный файл
                                    # w значит write (запись),
                                    # a — это appending (добавление данных к уже существующему файлу),
                                    # r — reading (чтение).

# Переименование файлов
# Переименовать text.txt на renamed-text.txt
# os.rename("text.txt", "renamed-text.txt")

# Перемещение файлов
# Заменить (переместить) этот файл в другой каталог
# os.replace("renamed-text.txt", "folder/renamed-text.txt")

# Удаление файлов
# удалить этот файл
# os.remove("folder/renamed-text.txt") # os.remove() удалит файл с указанным именем (не каталог).

# Удаление вложенных папок
# os.removedirs("nested1/nested2/nested3") # удалит только пустые каталоги

# Получение информации о файлах
# вывести некоторые данные о файле
# print(os.start("text.txt")) # это вернет кортеж с отдельными метриками. В их числе есть следующее:
                            # st_size — размер файла в байтах
                            # st_atime — время последнего доступа в секундах (временная метка)
                            # st_mtime — время последнего изменения
                            # st_ctime — в Windows это время создания файла, а в Linux — последнего
                                        # изменения метаданных
# Для получения конкретного атрибута нужно писать следующим образом:
# например, получить размер файла
# print("Размер файла:", os.start("text.txt").st_size)
