"""
Задача 1: Обмеження швидкості

Опис:
Користувач вводить швидкість автомобіля (в км/год).
Програма має виводити:

    До 50 км/год → "Місто"

    Від 51 до 90 → "Траса"

    Від 91 і більше → "Автобан"

    Менше 0 → "Помилка: некоректна швидкість"

Закріплюємо: if/elif/else, логічні вирази, введення.
"""

speed = int(input('Type speed: '))

if speed < 50:
    print('Town')
elif speed > 51 and speed < 90:
    print('Trasa')
elif speed > 91:
    print('Autoban')
else:
    print('ERROR')

"""
Задача 2: Перевірка стану акумулятора

Опис:
Є змінна battery_level (від 0 до 100).
Вивести:

    > 75: "Повний заряд"

    > 50: "Більше половини"

    > 25: "Менше половини"

    <= 25: "Низький заряд"

Додатково: якщо is_charging == True, додати фразу "Заряджається..."
"""

is_charging = True
battery_level = int(input('Type battery level: '))

if is_charging == True:
    print('Заряджається...')

if battery_level > 75:
    print('Повний заряд')
elif battery_level > 50:
    print('Більше половини')
elif battery_level > 25:
    print('Менше половини')
elif battery_level <= 25:
    print('Низький заряд')


"""
Задача 3 (комплексна): Автострахування

Опис:
Користувач вводить:

    Вік водія (int)

    Стаж водія (int)

    Кількість ДТП за останній рік (int)

Умови тарифу:

    Якщо вік < 18 → "Керування заборонено"

    Якщо вік >= 18 і стаж < 1 → "Новачок — тариф x2"

    Якщо ДТП > 0 → "Ризикований водій — тариф x1.5"

    Інакше — "Стандартний тариф"

Задача: розрахувати підсумковий тариф. Базовий тариф — 1000 грн.
Можна комбінувати множники (наприклад, новачок із ДТП — x3).
"""

base_price = 1000
tariff = 1

age = int(input('Вік водія: '))
experience = float(input('Стаж водія (у роках): '))
accidents = int(input('Кількість ДТП за рік: '))

if age < 18:
    print('Керування заборонено')
else:
    if experience < 1:
        tariff *= 2
        print('Новачок — тариф x2')
    if accidents > 0:
        tariff *= 1.5
        print('ДТП — тариф x1.5')

    final_price = base_price * tariff
    print('До сплати:', final_price, 'грн')


"""
Задача 4: Система попереджень на панелі авто

Опис:
Є кілька булевих змінних:

check_engine = True
low_oil = False
door_open = True

Завдання:

    Вивести відповідні попередження:
    "Перевірте двигун", "Низький рівень масла", "Двері відкриті"

Додатково: Якщо всі False, вивести "Все добре!"
"""

check_engine = False
low_oil = False
door_open = False

warnings = False

if check_engine:
    print('Перевірте двигун')
    warnings = True
if low_oil:
    print('Низький рівень масла')
    warnings = True
if door_open:
    print('Двері відкриті')
    warnings = True

if not warnings:
    print('Все добре!')
