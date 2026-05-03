import random

nested_list = [[random.randint(0, 10) for _ in range(4)] for _ in range(3)]
search_value = int(input("Введите значение для поиска: "))
print(f"Список: {nested_list}")

positions = []
i = 0
while i < len(nested_list):
    j = 0
    while j < len(nested_list[i]):
        if nested_list[i][j] == search_value:
            positions.append((i, j))
        j += 1
    i += 1

if positions:
    print(f"Значение {search_value} найдено в позициях: {positions}")
else:
    print(f"Значение {search_value} не найдено в списке.")