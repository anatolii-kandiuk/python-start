import math

"""
Задача 1: Автомобільний пробіг

Опис:
Водій щодня їздить 100 км. Порахуй, скільки днів потрібно, щоб проїхати відстань, введену користувачем (наприклад, 750 км), використовуючи while.
"""
print('\nTASK 1\n')
distance = float(input('Type the distance (km): '))
day_count = 0

while distance > 0:
    day_count += 1
    distance -= 100

print("Потрібно днів:", day_count)

# PRO Option to solve
"""

math.ceil() - ф-ція для заокруглення чисел до більшого значення 7.3 -> 8, 7.8 -> 8, ...

"""
print('\nЗ використанням ceil()')

distance = float(input("Type the distance (km): "))
day_count = math.ceil(distance / 100)
print("Потрібно днів:", day_count)

"""
Задача 2: Пошук авто в списку

garage = ["Opel", "Mazda", "Tesla", "BMW", "Audi"]

Користувач вводить назву машини. Програма шукає її у списку:

    Якщо є — виводить "Авто знайдене на X позиції"

    Якщо ні — "Немає в гаражі"

Використати: цикл for, break, else.
"""
print('\nTASK 2\n')

garage = ["Opel", "Mazda", "Tesla", "BMW", "Audi"]
user_auto = str(input('Type name of auto: '))

for index, auto in enumerate(garage, start=1):
    if auto == user_auto:
        print(f"Авто знайдене на {index} позиції")
        break
else:
    print("Немає в гаражі!")  
    
# enumerate() — це вбудована функція Python, яка додає індекси до елементів ітерабельного об'єкта (наприклад, списку, рядка або кортежу), 
#               щоб ти міг одразу отримати і індекс, і значення в циклі.


"""
Задача 3: Заряд акумулятора

Акумулятор заряджається по 10% щохвилини.
Початковий рівень — 30%.
Симулюй зарядку до 100%, виводячи статус кожної хвилини.

Додатково: якщо досягнуто 80%, вивести попередження: "Можна вже їхати"
"""

print('\nTASK 3\n')

lvl_of_charge = 30

while lvl_of_charge != 100:
    lvl_of_charge += 10
    print(f'Charge is: {lvl_of_charge} %')


"""
Задача 4 (комплексна): Обслуговування автопарку

У тебе є список авто з пробігом:

fleet = [
    {"model": "BMW", "km": 120000},
    {"model": "Tesla", "km": 80000},
    {"model": "Audi", "km": 145000},
    {"model": "Opel", "km": 98000}
]

Завдання:

    Для кожного авто визначити, чи потрібно ТО (якщо пробіг > 100_000)

    Порахувати загальний пробіг усього автопарку

    Вивести список авто, які ще "на ходу"
"""

print('\nTASK 4\n')

fleet = [
    {"model": "BMW", "km": 120000},
    {"model": "Tesla", "km": 80000},
    {"model": "Audi", "km": 145000},
    {"model": "Opel", "km": 98000}
]

total_km = 0
on_the_road = []

for auto in fleet:
    model = auto['model']
    km = auto['km']

    total_km += km

    if km > 100000:
        print(f'Необхідне ТО для {model}!')
    else:
        on_the_road.append(model)

print(f'\nЗагальний пробіг {total_km}')
print("Авто на ходу:", ', '.join(on_the_road))


"""
Домашнє завдання:

    Створи симулятор заправки:

        Ємність баку — 60 л

        Заправка йде по 5 л за крок

        Виводити статус після кожного кроку

        Коли бак повний — зупинити цикл і вивести: "Заправку завершено"
"""
print('\nTASK 5\n')

tank_lvl = 0

for tank_lvl in range(0, 61, 5):
    print(f'Tank lvl is: {tank_lvl} l')
else: 
    print('Заправку завершено')