# Ввод числа как строки для удобства разбор по цифрам
number = input("Введите натуральное число: ")

count_3 = 0
count_last_digit = 0
count_even = 0
sum_gt_5 = 0
product_gt_7 = 1
count_0_and_5 = 0

last_digit = number[-1]

# Перебмраем все цифры
for digit_char in number:
    digit = int(digit_char)

    # Количество цифр 3
    if digit == 3:
        count_3 += 1

    # Количество встреч последней цифры
    if digit_char == last_digit:
        count_last_digit += 1

    # Количество четных цифр
    if digit % 2 == 0:
        count_even += 1

    # Сумма цифрр больших пяти
    if digit > 5:
        sum_gt_5 += digit

    if digit > 7:
        if product_gt_7 == 1:
            product_gt_7 = digit
        else:
            product_gt_7 *= digit

    # Считаем число 0 и 5
    if digit_char == '0' or digit_char == '5':
        count_0_and_5 += 1

# Вывод результатов
print(count_3)
print(count_last_digit)
print(count_even)
print(sum_gt_5)
print(product_gt_7)
print(count_0_and_5)