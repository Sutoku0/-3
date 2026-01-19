n = int(input("Введите число n (длина последовательности): "))

max_num = 0
second_max = 0

for _ in range(n):
    num = int(input("Введите число: "))
    if num > max_num:
        second_max = max_num
        max_num = num
    elif num > second_max:
        second_max = num

print("Наибольшее число:", max_num)
print("Второе наибольшее число:", second_max)