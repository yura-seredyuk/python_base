""" 1. Скласти програму ’Атракціони’. 
    Програма запитує суму (грн.) у користувача. 
    Потім виводить на екран перелік доступних атракціонів. 
    Користувач обирає атракціон та ’оплачує’ його. 
    Вихід з програми при виборі пункту ’вихід’ або при недостатній сумі грошей."""


class NoMoney(Exception):
    pass


def calculate(money, price):
    if money >= price:
        money -= price
        print(f'You have UAH {money} left')
    else:
        raise NoMoney
    return money


try:
    money = float(input("Enter how much money you have: "))
    exit = False
    while not exit:
        choice = int(input(
            "Select attraction:\n\t1. roller coaster 50\n\t2. Ferris wheel 40\n\t3. pirate ship 30\n\t4. cars 20\n\t5. shooting gallery 10\n\t0. exit\n :-->> "))
        if choice == 1:
            money = calculate(money, 50)
        elif choice == 2:
            money = calculate(money, 40)
        elif choice == 3:
            money = calculate(money, 30)
        elif choice == 4:
            money = calculate(money, 20)
        elif choice == 5:
            money = calculate(money, 10)
        elif choice == 0:
            print("Bye!")
            exit = True
        else:
            print('Wrong choice. Please try again.')

except ValueError:
    print("\nERROR! Incorrect data. Only numbers can be entered.")
except NoMoney:
    print("\nYou do not have enough money. Bye!")
