USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """Конвертация долларов в рубли."""
    return amount_usd * USD_TO_RUB

amount = float(input("Введите сумму в долларах: "))
print(f"{amount} USD = {convert_usd_to_rub(amount):.2f} RUB")