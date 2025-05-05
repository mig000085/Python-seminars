# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def func(year):
    return 'yes' if year % 400 == 0 or year % 4 == 0 and  year % 100 != 0 else 'no'
        
print(func (2024))

# Константы для проверки високосного года
GREGORIAN_START = 1582
DIVISOR_4 = 4
DIVISOR_100 = 100
DIVISOR_400 = 400

year = int(input("Введите год: "))

if year < GREGORIAN_START:
    is_leap = False
elif year % DIVISOR_400 == 0:
    is_leap = True
elif year % DIVISOR_100 == 0:
    is_leap = False
elif year % DIVISOR_4 == 0:
    is_leap = True
else:
    is_leap = False

print(f"{year} год {'високосный' if is_leap else 'не високосный'}.")