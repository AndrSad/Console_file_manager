"""
- В том же проекте создать модуль test_filemanager.py для
тестирования функций консольного файлового менеджера.
- В файле написать тесты для каждой ""чистой"" функции, чем больше
тем лучше. Это могут быть функции консольного файлового менеджера,
а так же программы мой счет и программы викторина.
- (Дополнительно*) так же попробовать написать тесты
для ""грязных"" функций, например копирования файла/папки, ...
"""

import os
import platform
import shutil
from filemanager import mk_dir, rm_dir, copy_file, rename_file, remove_file

def test_mk_dir():
    assert mk_dir('folder1') == None


def test_rm_dir():
    assert rm_dir('folder1') == None


def test_copy_file():
    assert copy_file('text.txt', 'text_new.txt') == 'text_new.txt'


def test_rename_file():
    assert rename_file("text_new.txt", "text_rename.txt") == "text_rename.txt"


def test_remove_file():
    assert remove_file("text_rename.txt") == None


