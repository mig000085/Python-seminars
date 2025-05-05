import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.isqrt(num) + 1
    for d in range(3, max_divisor, 2):
        if num % d == 0:
            return False
    return True

n = int(input("Введите количество чисел: "))
count = 0

for _ in range(n):
    num = int(input("Введите число: "))
    if is_prime(num):
        count += 1

print(f"Количество простых чисел в последовательности: {count}")