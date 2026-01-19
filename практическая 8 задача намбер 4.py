m = int(input("Введите стартовое количество организмов (m): "))
p = int(input("Введите среднесуточный рост в процентах (p): "))
n = int(input("Введите количество дней (n): "))

population = m
for day in range(1, n + 1):
    print(f"{day} {population}")
    population += population * p / 100
