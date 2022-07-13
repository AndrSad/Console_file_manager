# global account
account = 0
def account_refill():
    refill = int(input('Введите сумму пополнения счета: '))
    global account
    account += refill

purchases = {}
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

def my_bank():
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
            break
        else:
            print('Неверный пункт меню.')
    print()
    print('----------')