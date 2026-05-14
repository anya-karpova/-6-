#8.4.4 Задача №3. Сортировка пузырьком.
#Сгенерируйте случайный массив длиной N=10. Отсортируйте его с помощью алгоритма сортировки пузырьком

#Сгенерируйте массивы разной длины (10,100,1000,10000, 100000). Замерьте время работы сортировки пузырьком. 
# Сделайте вывод о времени работы алгоритма.
import random
import time
def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr10 = [random.randint(1, 1000) for _ in range(10)]
print("Массив из 10 элементов:", sort(arr10))

s = [10, 100, 1000, 10000]
for n in s:
    arr = [random.randint(1, 1000) for i in range(n)]

    start = time.time()
    sort(arr)
    finish = time.time()

    time1 = finish - start

print(f"n = {n}, время = {time1:.6f} сек")



