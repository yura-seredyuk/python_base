""" 2. Користувач вказує ціну однієї хвилини вихідного дзвінка з одного
    мобільного оператора іншому, а також тривалість розмови. 
    Необхідно обрахувати грошову сумму, на яку був здійснений дзвінок"""

try:
    price = float(input("Enter the price of one minute of conversation: "))
    hours = int(input("Set the talk time:\n\thours: "))
    minutes = int(input("\tminutes: "))
    seconds = int(input("\tseconds: "))

    if price <= 0 or hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError

    if seconds > 0 and seconds <= 60:
        minutes += 1
    elif seconds > 60:
        minutes += seconds // 60
        if seconds % 60 > 0:
            minutes += 1
    cost = (hours * 60 + minutes) * price
    
    print("You need to pay: ", cost)
except ValueError:
    print("\nERROR! Incorrect data. Only positive numbers can be entered.")
