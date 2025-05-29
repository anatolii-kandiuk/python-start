##### Math and data types
print('\n[=============================================================]\n')
print('[Data Types 1]')
print('\n[=============================================================]\n')

print('\tMath opeerations: ')

input('Type \'Start\'==> ')

print('2+2', 2+2, sep='=', end='!\n')
print('2-2', 2-2, sep='=', end='!\n')
print('2*2', 2*2, sep='=', end='!\n')
print('2/2', 2/2, sep='=', end='!\n')
print('2%2', 2%2, sep='=', end='!\n')
print('2**2', 2**2, sep='=', end='!\n')
print('min([1, 2, 0, 5, -6])', min([1, 2, 0, 5, -6]), sep='=', end='!\n')
print('max([1, 2, 0, 5, -6])', max([1, 2, 0, 5, -6]), sep='=', end='!\n')
print('abs(-56)', abs(-56), sep='=', end='!\n')
print('pow(2, 4)', pow(2, 4), sep='=', end='!\n')
print('round(4.65)', round(4.65), sep='=', end='!\n\n\n')
 
###### Task 1: Car Cost Calculator
"""
Description:
    The user enters:

    * mileage (km)
    * fuel consumption per 100 km
    * price per 1 liter of fuel

Task: calculate the cost of the trip and display the result.
"""
print('1] Car Cost Calculator')

mileage = float(input("Type mileage (km) => "))
fuel_consumption = float(input("Type fuel consumption per 100 km => "))
price = float(input("Type price per 1 liter of fuel => "))

# Обчислення вартості поїздки
cost_of_the_trip = (mileage / 100) * fuel_consumption * price

print("\nResult: ", round(cost_of_the_trip, 2), "currency units")

"""
Пояснення:

    * mileage / 100 — скільки сотень кілометрів буде проїдено;

    * fuel_consumption — скільки літрів пального буде витрачено;

    * price — вартість цього пального;

"""

###### Task 2: Simple vehicle telemetry
"""
Description:
    Given variables:

    * speed = 90 # km/h
    * time = 2.5 # hours
    * fuel_rate = 8.5 # liters per 100 km

Task: calculate the distance
How much fuel did the car use?
What is the remaining fuel if the tank was full (60 l)?
"""
print('\n2] Simple vehicle telemetry')

speed = 90  
time = 2.5  
fuel_rate = 8.5  
tank_capacity = 60

distance = speed * time 
fuel_used = (fuel_rate / 100) * distance 
fuel_remaining = tank_capacity - fuel_used 

print("speed = 90 \ntime = 2.5 \nfuel_rate = 8.5 \ntank_capacity = 60 \n")
print("How much fuel did the car use?", fuel_used, sep=' |==> ')
print("What is the remaining fuel if the tank was full (60 l)?", fuel_remaining, sep=' |==> ')


###### Task 3 (complex): Parking lot
"""
Description:
    The car was left in the parking lot for a certain number of hours.

    * Price for the first 2 hours — 20 UAH/hour
    * Then — 15 UAH/hour
    * If it is night (00:00–06:00), additional -50%

Input: number of hours and time of day (day/night)
"""
print('\n3] Parking lot ')

hours = int(input("Count of hours? "))
time_of_day = input("Day or night (D/N): ").strip().upper()

first_two_hours_rate = 20
after_two_hours_rate = 15

if hours <= 2:
    cost = hours * first_two_hours_rate
else:
    cost = 2 * first_two_hours_rate + (hours - 2) * after_two_hours_rate

if time_of_day == 'N':
    cost *= 0.5

print("Result: ", round(cost, 2), "UAH")

print('\n[=============================================================]\n')
print('[Data Types 2]')
print('\n[=============================================================]\n')

"""
Задача 1: Конфігуратор автомобіля

Опис:
Запроси у користувача такі дані:

    Марка авто (str)
    Рік випуску (int)
    Ціна (float)
    Чи електро? (bool через так/ні)

Виведи:

    Тип кожної змінної
    Короткий опис:
    Ваш автомобіль Tesla 2020 року коштує 45600.0 €. Електро: True.
"""

auto_logo = input('Марка вашого авто |==> ')
year_present = int(input('Рік випуску |==> '))
price = float(input('Ціна |==> '))
is_electric = bool(input('Електроавтомобіль ? |==> '))

print(type(auto_logo), type(year_present), type(price), type(is_electric))
print('Ваш автомобіль {} {} року, коштує {}. Електро: {}'.format(auto_logo, year_present, price, is_electric))

"""
Задача 2: Конвертер кілометрів у милі та інші одиниці

Опис:
Користувач вводить відстань у км. Програма виводить:

    В милях (1 км = 0.621371 миль)

    У метрах

    У сантиметрах

    Вивести тип кожного результату.
"""

print('\nkm converter\n')
num = float(input('Type number km |==> '))
ONE_MILE_IN_KM = 0.621371

print('Mile: ', num * ONE_MILE_IN_KM)
print('SM: ', num * 100000)
print('M: ', num * 1000)

"""
Задача 3 (комплексна): Автомобільний аукціон

Опис:
Є 3 автомобілі з такими характеристиками:

car1_name = "BMW"
car1_year = 2018
car1_price = 22000.50

car2_name = "Audi"
car2_year = 2020
car2_price = 27000.00

car3_name = "Tesla"
car3_year = 2021
car3_price = 32000.99

Завдання:

    Обчисли середню ціну авто

    Знайди найновіше авто

    Створи змінну description з рядком:
    Tesla (2021) – 32000.99 €
"""

car1_name = "BMW"
car1_year = 2018
car1_price = 22000.50

car2_name = "Audi"
car2_year = 2020
car2_price = 27000.00

car3_name = "Tesla"
car3_year = 2021
car3_price = 32000.99

avg_price = (car1_price + car2_price + car3_price) / 3

print('AVG price: {}'.format(avg_price))

if (car1_year > car2_year & car1_year > car3_year):
    print( '{} ({}) - {} €'.format(car1_name, car1_year, car1_price))
elif (car2_year > car1_year & car2_year > car3_year):
    print( '{} ({}) - {} €'.format(car2_name, car2_year, car2_price))
else:
    print( '{} ({}) - {} €'.format(car3_name, car3_year, car3_price))
