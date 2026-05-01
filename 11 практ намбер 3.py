# Создаем словарь пятой степени чисел от 1 до 150 для быстрого поиска
powers = {i**5: i for i in range(1, 151)}

# Перебираем возможные значения для a, b, c, d с помощью вложенных циклов for
for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):  # начиная с a, чтобы избежать повторений
        b5 = b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                d5 = d ** 5
                sum_4 = a5 + b5 + c5 + d5
                # Проверяем, есть ли число e, такое что e^5 = сумма
                if sum_4 in powers:
                    e = powers[sum_4]  # получаем число e
                    # Проверка, что e в диапазоне
                    if 1 <= e <= 150:
                        # Вывод результата
                        print(f"Найдены числа: a={a}, b={b}, c={c}, d={d}, e={e}")
                        print(f"Сумма: {a + b + c + d + e}")
                        break  # Выходим из вложенных циклов по необходимости
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break