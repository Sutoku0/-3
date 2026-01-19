import random

secret_number = random.randint(1, 11)

for attempt in range(1, 4):
    guess = int(input(f"Попытка {attempt}: ").strip())
    if guess == secret_number:
        print("Угадали!")
        break
    else:
        if guess < secret_number:
            print("Неверно. Задайте число побольше.")
        else:
            print("Неверно. Задайте число поменьше.")
else:
    # Если цикл завершился без `break`, значит число не угадано
    print(f"Не угадали. Загаданное число было: {secret_number}")