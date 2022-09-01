"""
УРОК 8
0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала;
1. Где это возможно переписать код с использованием генераторов и тернарных операторов;
2. Там где возможны исключительные ситуации добавить обработку исключений;
3. *Где это возможно применить декораторы.
Иногда может быть так, что применить новые возможности негде, особенно декораторы - это нормально.
"""

print()
def my_filter(iterable, function):
    """
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True,
    то элемент входит в новую последовательность иначе False.
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    return (True if filter(function, iterable) else False)

print(my_filter([1, 2, 3, 4, 5], lambda x: (x > 3) == [4, 5]))
print(my_filter([1, 2, 3, 4, 5], lambda x: (x == 2) == [2]))
print(my_filter([1, 2, 3, 4, 5], lambda x: (x != 3) == [1, 2, 4, 5]))
print(my_filter(['a', 'b', 'c', 'd'], lambda x: (x in 'abba') == ['a', 'b']))


print()
numbers = []
for i in range(1, 11):
    number = int(input("Введите любое число от 0 до 9: "))
    numbers.append(number)
print(numbers)
print('Число 5 вводилось' if 5 in numbers else 'Число 5 не вводилось')


print()
sum_5 = 0
for i in range(1, 11):
    number = input("Введите любое число от 0 до 9: ")
    sum_5 = (sum_5 + 1 if number == "5" else sum_5 + 0)
print('Колличество введеных цыфр 5 равно:', sum_5)


print()
s = 0
numbers = [4, 5, 9, 5, 7, 4, 5, 7, 5, 8, 0, 5]
sum_5 = sum(1 if i == 5 else 0 for i in numbers)
print('Колличество цыфр 5 равно:', sum_5)


print()
SUM_NUMBE = 0
SUM_NUMBE = sum(SUM_NUMBE + i for i in range(1, 101))
print("Сумма ряда чисел от 1 до 100 равна: ", SUM_NUMBE)


print()
SUM_61 = 0
numbers_str = [4, 5, 9, 5, 7, 4, 5, 7, 5, 8, 0]
SUM_61 = sum(i for i in numbers_str)
print("Сумма всех цифр числа", numbers_str, "равна: ", SUM_61)


print()
SUM_63 = 0
number_int = 36419854
number_str = str(number_int)
SUM_63 = sum(int(y) for y in number_str)
print("Сумма всех цифр числа", number_int, " равна: ", SUM_63)


print()
number_8 = input("Введите любое 5-9значное число: ")
num_5 = 0
for i in number_8:
    if i == "5":
        num_5 += 1
    else:
        num_5 += 0
print('Цифра 5 есть в веденном числе' if num_5 >= 1 else 'Цифры 5 нет в веденном числе')


print()
while True:
    try:
        MULTI_71 = 1
        numbers_str = input("Введите любое 6-значное число: ")
        for i in numbers_str:
            MULTI_71 = MULTI_71 * int(i)
    except ValueError:
        print('Вы ввели не число. Введите верное число.')
    else:
        print("Произведение всех цифр числа", numbers_str, "равна: ", MULTI_71)


print()
while True:
    try:
        SUM_61 = 0
        numbers_str = input("Введите любое 5-9значное число: ")
        for i in numbers_str:
            SUM_61 = SUM_61 + int(i)
    except ValueError:
        print('Вы ввели не число. Введите верное число.')
    else:
        print("Сумма всех цифр числа", numbers_str, "равна: ", SUM_61)


print()
while True:
    try:
        list_lesson_31 = []
        quantity = int(input("Введите количество элементов: "))
        for i in range(quantity):
            i = int(input("Введите любое число: "))
            list_lesson_31.append(i)
    except ValueError:
        print('Вы ввели не число. Введите верное число.')
    else:
        list_lesson_31.sort()
        print(list_lesson_31)



