""" 1.Дано витрати машиною пального на 100 км, 
    ціну 1 л пального, а також шлях, який потрібно проїхати водію. 
    Обчислити та вивести на екран скільки потрібно витратити грошей 
    водію, щоб проїхати вказаний шлях."""

try:
    fuel_consumption = float(input("Specify fuel consumption per 100 km: "))
    fuel_price = float(input("Specify the price for fuel: "))
    distance = float(input("Specify the distance in kilometers: "))

    if fuel_consumption <= 0 or fuel_price <= 0 or distance <= 0:
        raise ValueError

    cost = fuel_consumption / 100 * distance * fuel_price

    print("You need to pay: ", cost)
except ValueError:
    print("\nERROR! Incorrect data. Only numbers greater than 0 can be entered.")
