""" 2. Скласти програму ’Банкомат’. 
    Програма запитує пароль (у вигляді числа) у користувача. 
    Якщо пароль вірний, то працює меню з пунктів: 
    поточний баланс, зняти гроші, вихід"""

money = 1000
exit = False
wrong = 0
try:
    while not exit and wrong < 3:
        password = int(input("Enter password\n :-->> "))
        if password != 1111:
            print('Wrong Password. Please try again.')
            wrong += 1
        else:
            print('Wrong choice. Please try again.')
            while not exit:
                choise = int(input(
                    "Welcome! Please select what to do:\n\t1. Show current balance\n\t2. Withdraw money\n\t0. Exit\n:-->> "))
                if choise == 1:
                    print(f'You have UAH {money}.')
                elif choise == 2:
                    sum = int(input("How much money do you need: "))
                    if sum > money:
                        print("You dont have enough money.")
                    else:
                        money -= sum
                        print("Take your money!")
                elif choise == 0:
                    exit = True
                    print("Bye!")
        if wrong == 3:
            print("Error! Your card is blocked!")
except ValueError:
    print("\nERROR! Incorrect data. Only integer numbers can be entered.")