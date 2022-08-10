
import math

def my_filter(iterable, function):
    """
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True,
    то элемент входит в новую последовательность иначе False.
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    if filter(function, iterable):
        return True
    else:
        return False


def my_pow(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power
    (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления
    """
    result = sum(args) ** power
    return result


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    result = simbol * count
    return result


def math_pow(number, degree):
    """
    Функция выполняет возведение числа number в степень degree и возвращает затем вещественный результат.
    :param number: число
    :param degree: степень
    :return: результат
    """
    result = math.pow(number, degree)
    return result


def math_sqrt(argument):
    """
    Возврат квадратного корня из аргумента
    :param argument: аргумент
    :return: результат
    """
    result = math.sqrt(argument)
    return result


def math_pi(d):
    """
    Представление математической константы π = 3.141592….
    "Пи" — это отношение длины окружности к её диаметру.
    :param d: диаметр окружности
    :return: результат
    """
    result = math.pi*d**2
    return result
    

def math_hypot(cathet1, cathet2):
    """
    Функция вычисляет гипотенузу треугольника c катетами cathet1 и cathet2.
    :param cathet1: катет 1
    :param cathet2: катет 2
    :return: hypotenuse гипотенуза
    """
    hypotenuse = math.hypot(cathet1, cathet2)
    return hypotenuse


def sorted_data(*args):
    """
    Функция сортировки данных.
    :param args: данные для сортировки
    :return: результат сортировки
    """
    result_sort = sorted(args)
    return result_sort


def f_map(args):
    """

    :param args:
    :return:
    """
    new_list = list(map(int, args))
    return new_list




