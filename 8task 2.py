number = 179
chars = ['X', 'Y', 'Z']
length = 5
base = 3
index = number - 1

# Изначально пустая строка
name = ''

# Проходим по каждому символу
for i in range(length):
    # Находим индекс символа на позиции i
    position = (index // (base ** (length - i - 1))) % base
    # Добавляем символ к имени
    name += chars[position]

print(name)