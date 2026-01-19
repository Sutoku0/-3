n = int(input("Введите натуральное число n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i

result = total * n
print(f"Значение суммы для n={n} равно: {result}")