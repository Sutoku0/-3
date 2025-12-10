input_str = input("Введите ваш вес в кг и рост в метрах через пробел: ")

weight, height = map(float, input_str.split())

bmi = weight/(height ** 2)

formatred_bmi = f"{bmi:1f}"

print(f"Ваш индекс массы тела (ИМТ): {formatred_bmi}")