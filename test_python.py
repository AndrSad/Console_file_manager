"""
- В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot. Чем
больше тестов на каждую функцию - тем лучше
"""

import math
from my_functions import my_filter, my_pow, separator, math_pow, math_sqrt, math_pi, math_hypot,\
                         sorted_data, f_map


def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: (x > 3) == [4, 5])
    assert my_filter([1, 2, 3, 4, 5], lambda x: (x == 2) == [2])
    assert my_filter([1, 2, 3, 4, 5], lambda x: (x != 3) == [1, 2, 4, 5])
    assert my_filter(['a', 'b', 'c', 'd'], lambda x: (x in 'abba') == ['a', 'b'])


def test_my_pow():
    assert my_pow(1, 1, 2) == 3
    assert my_pow(1, 2, 3) == 5
    assert my_pow(2, 1, 1) == 4
    assert my_pow(3, 2) == 8
    assert my_pow(2, 1, 2, 3, 4) == 100


def test_separator():
    assert separator('-', 10) == '----------'
    assert separator('#', 5) == '#####'
    assert separator('*', 10) == '**********'


def test_math_pow():
    assert math_pow(2, 3) == 8
    assert math_pow(4, 2) == 16
    assert math_pow(8, 5) == 32768
    assert math_pow(5, 5) == 5**5
    assert math_pow(10, 3) == 1000
    assert math_pow(9, 2) == 81


def test_math_sqrt():
    assert math_sqrt(81) == 9
    assert math_sqrt(100) == 10
    assert math_sqrt(121) == 11
    assert math_sqrt(625) == 25
    assert math_sqrt(25) == 5
    assert math_sqrt(36) == 6
    assert math_sqrt(49) == 7


def test_math_pi():
    assert math_pi(10) == (10 ** 2) / 2 * math.tau
    assert math_pi(15) == (15 ** 2) / 2 * math.tau
    assert math_pi(23) == (23 ** 2) / 2 * math.tau
    assert math_pi(37) == (37 ** 2) / 2 * math.tau
    assert math_pi(55) == (55 ** 2) / 2 * math.tau


def test_math_hypot():
    assert math_hypot(3, 4) == 5
    assert math_hypot(7, 9) == math.sqrt(7 ** 2 + 9 ** 2)
    assert math_hypot(5, 11) == math.sqrt(5 ** 2 + 11 ** 2)
    assert math_hypot(21, 35) == math.sqrt(21 ** 2 + 35 ** 2)
    assert math_hypot(55, 70) == math.sqrt(55 ** 2 + 70 ** 2)


def test_sorted_data():
    assert sorted_data(1, 4, 5, 2, 456, 12) == [1, 2, 4, 5, 12, 456]
    assert sorted_data(15, 3, 5, 7, 9, 11, 42) == [3, 5, 7, 9, 11, 15, 42]
    assert sorted_data(1, 4, 3, 6, 2, 8, 32, 11) == [1, 2, 3, 4, 6, 8, 11, 32]
    assert sorted_data(1, -4, 5, -7, 9, 2) == [-7, -4, 1, 2, 5, 9]


def test_f_map():
    old_list = ['1', '2', '3', '4', '5', '6', '7']
    assert f_map(old_list) == [1, 2, 3, 4, 5, 6, 7]


