"""
🔹 Що таке список?

Список (list) — це змінний впорядкований набір елементів. Тобто ти можеш:

    Додавати нові елементи

    Видаляти або змінювати існуючі

    Ітерувати по списку

    Використовувати вбудовані методи (сортування, пошук тощо)

Синтаксис:

my_list = [1, 2, 3, 4]
cars = ["BMW", "Tesla", "Audi"]
mixed = [42, "hello", True]

🧠 Властивості списків

    Індексуються з 0

    Можуть містити будь-який тип даних

    Змінювані (mutable): можна змінювати значення елементів

    Можна перебирати в циклі

🔧 Основні операції зі списками

fruits = ['apple', 'banana', 'orange']

# Доступ за індексом
print(fruits[0])  # apple

# Зміна елемента
fruits[1] = 'grape'

# Додавання
fruits.append('kiwi')  # Додає в кінець

# Вставка в позицію
fruits.insert(1, 'lemon')

# Видалення по значенню
fruits.remove('orange')

# Видалення по індексу
del fruits[2]

# Довжина списку
print(len(fruits))

📌 Корисні методи списків
Метод	Опис
append(x)	Додає елемент x у кінець списку
insert(i, x)	Вставляє x на позицію i
remove(x)	Видаляє перше входження x
pop([i])	Видаляє елемент з індексом i (або останній)
clear()	Очищає список
index(x)	Повертає індекс першого x
count(x)	Рахує кількість входжень x
sort()	Сортує список
reverse()	Розвертає список
copy()	Копія списку
"""
###
"""
Задача 1: Найбільш населені столиці

У тебе є два списки:

cities = ["Berlin", "Paris", "Madrid", "Rome", "Vienna", "Warsaw"]
populations = [3_600_000, 2_100_000, 3_200_000, 2_870_000, 1_900_000, 1_790_000]

Завдання:

    Створи новий список тільки з міст, де населення більше ніж 2.5 млн.

    Виведи їх у відсортованому вигляді за спаданням населення.

    Підрахуй загальну кількість населення цих міст.
"""
###

cities = ["Berlin", "Paris", "Madrid", "Rome", "Vienna", "Warsaw"]
populations = [3_600_000, 2_100_000, 3_200_000, 2_870_000, 1_900_000, 1_790_000]

large_cities = []
large_populations = []

for city, population in zip(cities, populations):
    if population > 2_500_000:
        large_cities.append(city)
        large_populations.append(population)

sorted_cities = []
sorted_populations = []

while large_populations:
    max_index = large_populations.index(max(large_populations))
    
    sorted_cities.append(large_cities[max_index])
    sorted_populations.append(large_populations[max_index])
    
    large_cities.pop(max_index)
    large_populations.pop(max_index)

print("1-2) Міста з населенням понад 2.5 млн (за спаданням):")
for i in range(len(sorted_cities)):
    print(f"   - {sorted_cities[i]}: {sorted_populations[i]} мешканців")

total_population = sum(sorted_populations)
print("\n3) Загальна кількість населення цих міст:", total_population)


"""
Задача 2: Історичні події та роки

events = [
    ["Падіння Берлінської стіни", 1989],
    ["Місяцева місія Apollo 11", 1969],
    ["Друга світова війна закінчилася", 1945],
    ["Заснування ЄС", 1993],
    ["Перша Олімпіада", -776]
]

Завдання:

    Виведи всі події, які відбулися у XX столітті (1901–2000).

    Додай у список ще 2 події самостійно.

    Виведи список подій у хронологічному порядку.
"""
###
events = [
    ["Падіння Берлінської стіни", 1989],
    ["Місяцева місія Apollo 11", 1969],
    ["Друга світова війна закінчилася", 1945],
    ["Заснування ЄС", 1993],
    ["Перша Олімпіада", -776]
]

is_event = input("\nВи б хотіли ввести свою подію ? (y/n) | ==> ")

while is_event == 'y':

    event_name = input('Введіть назву події: ')
    event_year = int(input('Введіть рік події: '))

    events.append([event_name, event_year])

    is_event = input("Ви б хотіли ввести ще одну подію ? (y/n) | ==> ")

# events.append(["Заснування Києва", 482])
# events.append(["Проголошення незалежності України", 1991])

print("\nПодії XX століття:")
for event in events:
    if 1901 <= event[1] <= 2000:
        print(f"{event[0]} — {event[1]}")

unsorted_events = events[:]
sorted_events = []

while unsorted_events:
    earliest_year = unsorted_events[0][1]
    index_of_earliest = 0

    for i in range(1, len(unsorted_events)):
        if unsorted_events[i][1] < earliest_year:
            earliest_year = unsorted_events[i][1]
            index_of_earliest = i

    sorted_events.append(unsorted_events[index_of_earliest])
    unsorted_events.pop(index_of_earliest)

print("\nВсі події у хронологічному порядку:")
for event in sorted_events:
    print(f"{event[0]} — {event[1]}")

"""
Задача 3: Аналіз даних про населення

Є список населення деяких країн (в млн):

countries = ["Germany", "France", "Poland", "Italy", "Ukraine"]
population = [83, 67, 38, 60, 37]

Завдання:

    Знайди країну з найменшим і найбільшим населенням.

    Обчисли середнє населення.

    Виведи список країн, де населення вище середнього.

"""
###
countries = ["Germany", "France", "Poland", "Italy", "Ukraine"]
populations = [83, 67, 38, 60, 37]

max_population_index = populations.index(max(populations))
min_population_index = populations.index(min(populations))

avg_populations = sum(populations) / len(populations)

print(f'\nКраїна з найменшим {countries[min_population_index]} - {populations[min_population_index]} і \nнайбільшим {countries[max_population_index]} - {populations[max_population_index]} населенням.')
print(f'Середнє населення: {avg_populations}')

print(f'Список країн, де населення вище середнього.')
for country, population in zip(countries, populations):
    if population > avg_populations:
        print(' ', country)

"""
Задача 4 (математична): Вивід простих чисел

Завдання:

    Створи список чисел від 2 до 100.

    Створи новий список, куди увійдуть тільки прості числа (просте число — ділиться лише на 1 та на себе).

    Виведи довжину цього нового списку та його вміст.
"""

###
numbers = list(range(2, 101))
prime_numbers = []

for number in numbers:
    is_prime = True 

    for divisor in range(2, number):
        if number % divisor == 0: 
            is_prime = False 
            break 
    
    if is_prime:
        prime_numbers.append(number)

print(f'\nКількість простих чисел: {len(prime_numbers)}')
print('Прості числа від 2 до 100:')
print(prime_numbers)


"""
Домашнє завдання (інтегроване)

Задача: Німецький словник

Створи програму, яка:

    Має два списки: німецькі слова й українські переклади.

    Дає змогу користувачу ввести слово українською і отримати переклад.

    Реалізуй перевірку — якщо слова немає, вивести повідомлення: "Немає у словнику!"
"""