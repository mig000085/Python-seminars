# Выведите в консоль таблицу умножения 
# от 2х2 до 9х10 как на школьной тетрадке.

# for i in range(2, 10):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')
        
        
# for k in [0, 4]:
#     for i in range(2, 11):
#         res = ''
#         for j in range(2 + k , 6 + k ):
#             res += f'{j:^2}* {i * j:^2}\t'
#             print(res)
#     print()
    
# for i in range(2, 11):
#     left = "  ".join([f"{j} × {i}={j*i:2}" for j in range(2, 6)])
#     right = "  ".join([f"{j} × {i}={j*i:2}" for j in range(6, 10)])
#     print(f"{left}  |  {right}")


for i in range(2, 10):
    for j in range(1, 11):
        result = 1 * j
        print(f'{i} * {j} = {result}\t' , end="")
print()