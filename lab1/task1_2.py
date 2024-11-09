def knapsack_with_limited_items(N, W, items):

    # Ініціалізуємо масив dp для зберігання максимальної цінності для кожної ваги рюкзака
    dp = [0] * (W + 1)

    # Перебираємо кожен тип предметів
    for weight, value, max_count in items:
        # Для кожного предмета, перебираємо ваги рюкзака у зворотному порядку
        for current_weight in range(W, weight - 1, -1):
            # Перебираємо кількість предметів, які можна взяти (від 1 до max_count)
            for count in range(1, max_count + 1):
                if current_weight >= count * weight:
                    # Оновлюємо dp[current_weight], якщо можемо отримати більшу цінність
                    dp[current_weight] = max(dp[current_weight], dp[current_weight - count * weight] + count * value)

    # Повертаємо максимальну цінність, яку можна отримати для ваги W
    return dp[W]

# Приклад використання:
N = 3  # кількість типів предметів
W = 10  # максимальна вага рюкзака
# items = [(вага, цінність, максимальна кількість)]
items = [
    (2, 3, 4),  # предмет з вагою 2, цінністю 3, можна взяти до 4 разів
    (3, 4, 2),  # предмет з вагою 3, цінністю 4, можна взяти до 2 разів
    (5, 7, 1)   # предмет з вагою 5, цінністю 7, можна взяти до 1 разу
]

# Розрахунок і вивід результату
max_value = knapsack_with_limited_items(N, W, items)
print(f"Максимальна цінність для ваги рюкзака {W}: {max_value}")