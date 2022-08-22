import os
import platform
import shutil

def mk_dir(dir_name):
    # Создать пустой каталог (папку)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        return
    else:
        return print("Папка с таким именем уже существует.")


def rm_dir(dir_name):
    # Удаление директории/папки
    if os.path.isdir(dir_name):
        os.rmdir(dir_name)
        return
    else:
        print("Папки с таким именем не существует.")


def copy_file(old_file, new_file):
    # Копирование файла
    shutil.copyfile(old_file, new_file)
    return new_file


def rename_file(old_file, new_file):
    # Переименование файлов
    os.rename(old_file, new_file)
    return new_file


def remove_file(remove_file):
    # Удаление файлов
    os.remove(remove_file)
    return



