""" 4. Розробити програму, що переводить значення температури в градусах по Цельсію
    в температуру по Фаренгейту та навпаки. 
    Співвідношення між температурами визначається формулою: TF = TC *1.8 +32. 
    Діалог с користувачем реалізувати через систему меню."""

try:
    exit = False
    while not exit:
        choice = int(input(
            "Select what you want to convert:\n\t1. degrees Celsius to degrees Fahrenheit\n\t2. degrees Fahrenheit to degrees Celsius\n\t0. exit\n :-->> "))
        if choice == 1:
            celsius = float(input("Enter degrees Celsius:"))
            fahrenheit = round(celsius * 1.8 + 32, 2)
            print(f'{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit\n')
        elif choice == 2:
            fahrenheit = float(input("Enter degrees Fahrenheit:"))
            celsius = round((fahrenheit - 32) / 1.8, 2)
            print(f'{fahrenheit} degrees Celsius = {celsius} degrees Fahrenheit\n')
        elif choice == 0:
            print("Bye!")
            exit = True
        else:
            print('Wrong choice. Please try again.')

except ValueError:
    print("\nERROR! Incorrect data. Only numbers can be entered.")
