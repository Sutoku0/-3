# сам размер доски 8 на 8
size = 8
#перебираем строки и клетки
for row in range(size):
    for col in range(size):
        # Определяем цвет клетки
        if (row + col) % 2 == 0:
            print('W', end=' ')
        else:
            print('B', end=' ')
    print()