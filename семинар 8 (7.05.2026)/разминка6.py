input_list = ["kar", "meow", "https://rsmu.ru", "bioinf", "http://yandex.ru", "Russia"]
print(f"Исходный список {input_list}")
result_list = input_list.copy()
for item in input_list:
    if not item.startswith("http://"):
        result_list.remove(item)
print(f"Осталось {result_list}")