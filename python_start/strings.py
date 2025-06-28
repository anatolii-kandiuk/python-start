"""
🚀 Задача 1: Підрахунок голосних

Завдання:
Користувач вводить речення.
Порахуй кількість голосних у цьому реченні.

✔ Закріплюємо: цикл for, індекси, метод lower()
"""
###

user_msg = input("Type the text |=> ")
vowels = [
    'a', 'ä', 'e', 'ë', 'i', 'o', 'ö', 'u', 'ü', 'y', 
    'а', 'е', 'є', 'ё', 'и', 'і', 'ї', 'о', 'у', 'ы', 'э', 'ю', 'я' 
]

count_vowels = sum(1 for letter in user_msg if letter in vowels)

# count_vowels = 0
# for letter in user_msg:
#     if letter.lower() in vowels:
#         count_vowels += 1

print(f'Count of vowels: {count_vowels}\n')

"""
🗺️ Задача 2: Географічний аналіз

Завдання:
Є список міст:
cities = "Berlin, Paris, Rome, Warsaw, Madrid"

✔ Виведи окремо кожне місто (використовуй метод split).

✔ Знайди місто з найдовшою назвою (по довжині рядка).

✔ Виведи всі міста з великої букви, навіть якщо у списку вони написані з маленької.
"""
###
cities = "Berlin, Paris, rome, warsaw, Madrid"
cities_list = cities.split(', ')
longest_city = ""

print(cities_list)
print(cities.title())

for city in cities_list:
    if len(city) > len(longest_city):
        longest_city = city

print(f'Longest city is: {longest_city}\n')

"""
📜 Задача 3: Історичний текст

Завдання:
Є рядок:
text = "Die Geschichte Europas ist sehr vielfältig und spannend."

✔ Виведи тільки перші 15 символів.

✔ Замініть слово "Europas" на "der Ukraine".

✔ Підрахуй кількість літер e у всьому тексті.
"""
###
text = "Die Geschichte Europas ist sehr vielfältig und spannend."

print(text[:15])
print(text.replace('Europas', 'der Ukraine'))
print(f'Count of E in [{text}]: {sum(1 for letter in text if letter.lower() == "e")}')

"""
🔬 Задача 4 (складна, математична): Перевірка паліндромів

Завдання:
Користувач вводить слово.
Перевір, чи є воно паліндромом (читається однаково зліва направо і справа наліво).

✔ Використовуй зрізи для перевірки.
"""

user_word = input('Type the word: ').lower().replace(" ", "")

if user_word == user_word[::-1]:
    print(f'The word "{user_word}" is palindrom!')
else:
    print(f'The word "{user_word}" isn`t palindrom!')

"""
✨ Задача 5: Обчислення частоти букв

Користувач вводить текст. Потрібно:

    виділити всі латинські літери (ігноруючи пробіли, цифри, пунктуацію),

    порахувати, яка літера трапляється найчастіше,

    вивести її та кількість входжень.

📌 Порада: використай .lower(), .count() і цикл по set().
"""
###



"""
🧮 Задача 6 (математична): Цифри у тексті

Користувач вводить текст, який містить букви та числа.

Завдання:

    Знайди усі цифри в рядку.

    Виведи їх у порядку появи.

    Знайди суму цих цифр.

📌 Порада: символ — це цифра, якщо char.isdigit() повертає True.
"""

"""
🧬 Задача 7 (програмістська): Перевірка змінної

Користувач вводить рядок, який має бути назвою змінної в Python.

Перевір:

    чи рядок не починається з цифри

    чи не містить пробілів або символів окрім _ і букв

    чи не є ключовим словом Python (наприклад: for, while, def…)

📌 Порада: ключові слова можна отримати з модуля keyword:
"""

"""
🌐 Задача 8 (географічна): Стандартизація назв міст

cities = ["Berlin", "kIEv", "Wien", "paris", "MADRID"]

Завдання:

    Приведи всі назви до формату: перша літера велика, інші — малі.

    Виведи міста, які починаються на голосну (A, E, I, O, U).
"""