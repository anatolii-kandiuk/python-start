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