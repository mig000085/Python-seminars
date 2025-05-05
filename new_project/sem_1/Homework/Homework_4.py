n = int(input("Введите глубину ямы: "))

for i in range(n):
    # Количество точек по краям
    dots = '.' * i
    # Число для центральной части
    current_num = str(n - i)
    # Центральная часть: число, повторенное (n-i) раз через точки
    middle = '.'.join([current_num] * (n - i))
    # Собираем строку
    print(f"{dots}{middle}{dots}")