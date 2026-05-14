#8.4.4 Задача №3. Сортировка пузырьком.
#Сгенерируйте случайный массив длиной N=10. Отсортируйте его с помощью алгоритма сортировки пузырьком

#Сгенерируйте массивы разной длины (10,100,1000,10000, 100000). Замерьте время работы сортировки пузырьком. 
# Сделайте вывод о времени работы алгоритма.
import random
import time

arr = [random.randint(1, 100) for i in range(10)]

def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Массив из 10 элементов:", sort(arr))

all_time = 0

for n in [10, 100, 1000, 10000, 100000]:
    arr = [random.randint(1, 100) for i in range(10)]
    start = time.time()
    sort(arr)
    finish = time.time()
    time1 = finish - start
    all_time += time1

print("Время работы: " + str(all_time))



