def check_range(value, name):
    if not (1 <= value <= 8):
        print(f"Ошибка: {name} должно быть в диапазоне от 1 до 8.")
        exit()

column_first = int(input("Введите номер столбца первой клетки (от 1 до 8): "))
check_range(column_first, "номер столбца первой клетки")
row_first = int(input("Введите номер строки первой клетки (от 1 до 8): "))
check_range(row_first, "номер строки первой клетки")

column_second = int(input("Введите номер столбца второй клетки (от 1 до 8): "))
check_range(column_second, "номер столбца второй клетки")
row_second = int(input("Введите номер строки второй клетки (от 1 до 8): "))
check_range(row_second, "номер строки второй клетки")

first_cell_color = (column_first + row_first) % 2
second_cell_color = (column_second + row_second) % 2

if first_cell_color == second_cell_color:
    print("YES")
else:
    print("NO")