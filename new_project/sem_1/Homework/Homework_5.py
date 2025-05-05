start = 1
finish = 100
count = 0

print("Загадайте число от 1 до 100 (включительно).")
print("Отвечайте на вопросы: 1 — равно, 2 — больше, 3 — меньше.")

while True:
    n = (start + finish) // 2
    count += 1
    answer = int(input(f"Попытка {count}: Твоё число равно, больше или меньше, чем {n}? (1/2/3): "))
    
    if answer == 1:
        print(f"Ура! Число угадано за {count} попыток.")
        break
    elif answer == 2:
        start = n + 1
    elif answer == 3:
        finish = n - 1
    else:
        print("Некорректный ответ. Пожалуйста, введите 1, 2 или 3.")
        count -= 1  # Не засчитываем некорректную попытку
    
    if start > finish:
        print("Кажется, вы где-то ошиблись в ответах. Невозможно угадать число с такими ответами.")
        break