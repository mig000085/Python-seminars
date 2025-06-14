#Задание №4
#Работа в консоли в режиме интерпретатора Python.
#Решите квадратное уравнение 5x2-10x-400=0 последовательно
#сохраняя переменные a, b, c, d, x1 и x2.
#*Попробуйте решить уравнения с другими значениями a, b, c

from  math import sqrt

a = 5
b = -10
c = -400

d = (b ** 2) - (4 * a * c)
if d < 0:
    print('корней нет')
elif d > 0:
    x1 = (sqrt(d) -b) / (2 * a)
    x2 = (-sqrt(d) -b) / (2 * a)
    print(f'корни {x1, x2}')
elif d == 0:
    print((-b) / (2*a))
    
    
# Задаем коэффициенты уравнения
a = 5
b = -10
c = -400

# Вычисляем дискриминант
d = b**2 - 4*a*c

# Вычисляем корни уравнения
x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)

# Выводим результаты
print("Корни уравнения:")
print("x1 =", x1)
print("x2 =", x2)