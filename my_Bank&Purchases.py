
"""
УРОК 7, ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.
   При первом открытии программы на счету 0
   После того как мы воспользовались программой и вышли сохранить сумму счета
   При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл
   При первом открытии программы истории нет.
   После того как мы что-нибудь купили и закрыли программу сохранить историю покупок.
   При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""

import os
import json
FILE_BANK = 'my_bank.txt'
FILE_PURCHASES = 'my_purchases.txt'
JSON_PURCHASES = 'my_purchases.json'

if not os.path.isfile(FILE_BANK):
    account = 0
else:
    with open(FILE_BANK, 'r') as f:
        account = int(f.read())
        print(account)

def account_refill():
    refill = int(input('Введите сумму пополнения счета: '))
    global account
    account += refill
    return account

# if not os.path.isfile(FILE_PURCHASES): # Вариант 1:
if not os.path.isfile(JSON_PURCHASES): # Вариант 2: с использованием формата json

    purchases = {}

else:
    # with open(FILE_PURCHASES, 'r') as f: # Вариант 1:
    #     purchases = f.read()
    #     purchases = eval(purchases)

    with open(JSON_PURCHASES, 'r') as f: # Вариант 2: с использованием формата json
        purchases = json.load(f)

        print(purchases, type(purchases))


def my_purchases():
    global account
    global purchases
    purchase_price = int(input('Ведите стоимость покупки: '))
    if purchase_price <= account:
        account = account - purchase_price
        print('Остаток на счете:', account)
        purchase = my_purchase()
        print(purchase, purchase_price)
        purchases.update({purchase: purchase_price})
        print(purchases)
    else:
        print('Не достаточно средств на счете')
        pass

def my_purchase():
    global purchase
    purchase = input('Ведите наименование покупки: ')
    while purchases.get(purchase) != None:
        purchase = input('Ведите другое наименование покупки: ')
    else:
        return purchase


print('----------')
print()
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        account_refill()
        print('Текущее состояния счета:', account)
    elif choice == '2':
        my_purchases()
    elif choice == '3':
        print('История покупок:', purchases)
    elif choice == '4':
        with open(FILE_BANK, 'w') as f:
            f.write(str(account))
        # with open(FILE_PURCHASES, "w") as f: # Вариант 1:
        #     f.write(str(purchases))
        with open(JSON_PURCHASES, 'w') as f: # Вариант 2: с использованием формата json
            json.dump(purchases, f)
        break
    else:
        print('Неверный пункт меню.')
print()
print('----------')