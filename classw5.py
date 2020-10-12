""" 5. Написати повноцінний калькулятор. 
    Введення цифр та вибір математичної операції виконати в діалоговому стилі 
    (запитати у користувача, вивести меню). 
    У програмі передбачити уникнення помилок (ділення на нуль і т.д.)."""

try:
    exit = False
    while not exit:
        choice = int(input(
            "Select what you want to calculate:\n\t1. sum\n\t2. difference\n\t3. product\n\t4. division\n\t0. exit\n :-->> "))
        if choice == 1:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            rez = num1 + num2
            print(f'{num1} + {num2} = {rez}\n')
        elif choice == 2:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            rez = num1 - num2
            print(f'{num1} - {num2} = {rez}\n')
        elif choice == 3:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            rez = num1 * num2
            print(f'{num1} * {num2} = {rez}\n')
        elif choice == 4:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if num2 != 0:
                rez = num1 / num2
                print(f'{num1} / {num2} = {rez}\n')
            else:
                raise ZeroDivisionError
        elif choice == 0:
            print("Bye!")
            exit = True
        else:
            print('Wrong choice. Please try again.')

except ValueError:
    print("\nERROR! Incorrect data. Only numbers can be entered.")
except ZeroDivisionError:
    print("\nERROR! Division by Zero.")
