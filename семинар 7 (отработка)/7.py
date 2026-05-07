#Выведите все простые числа в заданном пользователем интервале
a = int(input("введите пожалуйста начало интервала:"))
b = int(input("введите пожалуйста конец интервала:"))
for i in range (a, b + 1):
    if i < 2:
        continue

    c = True

    for j in range(2, i):
        if i % j == 0:
            c = False
            break
    
    if c:
        print(i)










