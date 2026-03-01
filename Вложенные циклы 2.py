a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for divider in range(2, int(num ** 0.5) + 1):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            print(num)