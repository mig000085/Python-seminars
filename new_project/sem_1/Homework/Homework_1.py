width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

# Проверка минимальных размеров
if width < 2 or height < 2:
    print("Ошибка: ширина и высота должны быть не менее 2.")
else:
    for row in range(height):
        if row == 0 or row == height - 1:
            # Верхняя и нижняя границы
            print('-' * width)
        else:
            # Боковые границы с пробелами внутри
            print('|' + ' ' * (width - 2) + '|')