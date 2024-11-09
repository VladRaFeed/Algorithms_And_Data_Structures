# Функція для розв'язання задачі дробного рюкзака
def fractional_knapsack(weights, values, capacity):
    # Обчислюємо цінність на одиницю ваги для кожного предмета
    n = len(weights)
    value_per_weight = [(values[i] / weights[i], values[i], weights[i], i) for i in range(n)]
    
    # Сортуємо предмети за цінністю на одиницю ваги (від найбільшого до найменшого)
    value_per_weight.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0  # Загальна цінність
    remaining_capacity = capacity  # Залишкова місткість рюкзака
    fractions = [0] * n  # Масив для зберігання частки кожного предмета, який беремо
    
    for value_per_unit, value, weight, index in value_per_weight:
        if remaining_capacity == 0:
            break
        
        if weight <= remaining_capacity:
            # Якщо можемо взяти предмет повністю
            fractions[index] = 1
            total_value += value
            remaining_capacity -= weight
        else:
            # Якщо беремо частину предмета
            fraction = remaining_capacity / weight
            fractions[index] = fraction
            total_value += value * fraction
            remaining_capacity = 0
    
    return total_value, fractions

# Приклад використання
weights = [10, 20, 30]  # Ваги предметів
values = [60, 100, 120]  # Цінності предметів
capacity = 50  # Максимальна вага рюкзака

# Розв'язок задачі
max_value, fractions = fractional_knapsack(weights, values, capacity)

print("Максимальна цінність:", max_value)
print("Частка кожного предмета в рюкзаку:", fractions)