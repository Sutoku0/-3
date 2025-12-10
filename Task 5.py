banknotes = [5000, 2000, 1000, 500, 200, 100]
amount = int(input("Введите сумму (кратное 100): "))
if amount % 100 != 0:
    print("Ошибка.")
else:
    for note in banknotes:
        count = amount // note
        amount -= count * note
        print(f"{note} x {count}")
    if amount != 0:
        print("Не удалось выдать точную сумму.")