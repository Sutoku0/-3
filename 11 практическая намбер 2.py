# Стоимость животных
price_bull = 10
price_cow = 5
price_calf = 0.5

# Перебираем быков
for num_bulls in range(0, 11):  # максимум 10 быков
    # Перебираем коров
    for num_cows in range(0, 21):  # максимум 20 коров
        # Перебираем телят
        for num_calfs in range(0, 201):  # максимум 200 телят
            total_cost = (num_bulls * price_bull +
                          num_cows * price_cow +
                          num_calfs * price_calf)
            if total_cost == 100:
                print(f"Быков: {num_bulls}, Корова: {num_cows}, Телят: {num_calfs}")