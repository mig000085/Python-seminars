# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# while True:
#     num = int(input('введите число'))
#     if 1 < num > 999:
#         print('number out of range')
#         continue
#     elif 1 <= num < 10:
#         print(num ** 2)
#         break
#     elif 10 <= num < 100:
#         print((num % 10) * (num // 10))
#         break
#     elif 100 <= num  <= 999:
#         last = num % 10
#         num //= 10
#         middle = num % 10
#         first = num // 10
#         answer = last * 100 + middle * 10 + first
#         print(answer)
        
#Константы для диапазона и границ чисел
MIN_NUM, MAX_NUM = 1, 999

# Ввод числа с проверкой диапазона
number = int(input("Введите число от 1 до 999: "))
while not (MIN_NUM <= number <= MAX_NUM):
    number = int(input("Ошибка! Введите число от 1 до 999: "))

# Определение типа числа и вычисление результата
if number < 10:
    result = number ** 2
    category = "цифра"
elif number < 100:
    d1, d2 = number // 10, number % 10
    result = d1 * d2
    category = "двузначное число"
else:
    d1, d2, d3 = number // 100, (number // 10) % 10, number % 10
    result = d3 * 100 + d2 * 10 + d1
    category = "трёхзначное число"

print(f"{category}, результат: {result}")