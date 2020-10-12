""" 3. Написати програму, яка переводить повний оберт
    планети Марс навколо Сонця в земні роки. Оберти ввести з клавіатури. 
    (Марс робить повний оберт навколо Сонця за 686 земних днів)"""

try:
    mars_rotations_count = float(
        input("Set the number of revolutions of the planet Mars around the Sun: "))

    if mars_rotations_count <= 0:
        raise ValueError

    earth_years_count = round(mars_rotations_count * 686 / 365, 1)

    print(f'This period corresponds to {earth_years_count} Earth years')
except ValueError:
    print("\nERROR! Incorrect data. Only positive numbers can be entered.")
