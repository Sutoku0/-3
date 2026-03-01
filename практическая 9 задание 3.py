total_price = int(input("Короче скока стоит услуга Геральта"))
coin_denominations = [25, 10, 5, 1]
total_coins = 0
remaining_amount = total_price
i = 0

while remaining_amount > 0:
    if remaining_amount >= coin_denominations[i]:
        remaining_amount -= coin_denominations[i]
        total_coins += 1
    else:
        i += 1
        if i >= len(coin_denominations):
            break
else:
    print(f"Минимальное количество чеканных монет: {total_coins}")