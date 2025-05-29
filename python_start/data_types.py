##### Math and data types
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

first_2_hours_rate = 20
after_2_hours_rate = 15

if hours <= 2:
    cost = hours * first_2_hours_rate
else:
    cost = 2 * first_2_hours_rate + (hours - 2) * after_2_hours_rate

if time_of_day == 'N':
    cost *= 0.5

print("Result: ", round(cost, 2), "UAH")
