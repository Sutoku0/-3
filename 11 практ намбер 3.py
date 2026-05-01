# Создаем словарь пятой степени чисел от 1 до 150 для быстрого поиска
powers = {i**5: i for i in range(1, 151)}


for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):
        b5 = b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                d5 = d ** 5
                sum_4 = a5 + b5 + c5 + d5
                if sum_4 in powers:
                    e = powers[sum_4]
                    if 1 <= e <= 150:
                        print(f"Найдены числа: a={a}, b={b}, c={c}, d={d}, e={e}")
                        print(f"Сумма: {a + b + c + d + e}")
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break