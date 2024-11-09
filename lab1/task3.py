# Функція для обчислення значення виразу з двома операндами та оператором
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else float('-inf')  # Уникаємо ділення на 0



# Функція для знаходження максимального значення виразу
def maximize_expression(expression):
    # Розділення чисел та операторів
    numbers = []
    operators = []
    num = ""
    
    # Парсимо числа та оператори з вхідного виразу
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            numbers.append(float(num))
            operators.append(char)
            num = ""
    numbers.append(float(num))  # Додаємо останнє число

    n = len(numbers)
    # Ініціалізація таблиць для зберігання мінімальних і максимальних значень підвиразів
    max_vals = [[None] * n for _ in range(n)]
    min_vals = [[None] * n for _ in range(n)]

    # Заповнюємо діагональні елементи таблиць
    for i in range(n):
        max_vals[i][i] = numbers[i]
        min_vals[i][i] = numbers[i]

    # Динамічне заповнення таблиць для кожної довжини підвиразу
    for s in range(1, n):  # s - відстань між початком та кінцем підвиразу
        for i in range(n - s):
            j = i + s
            max_vals[i][j] = float('-inf')
            min_vals[i][j] = float('inf')
            
            # Розглядаємо всі можливі способи розбиття підвиразу на два
            for k in range(i, j):
                op = operators[k]
                
                # Обчислюємо всі можливі значення для різних комбінацій мінімальних і максимальних підвиразів
                possible_values = [
                    calculate(max_vals[i][k], max_vals[k + 1][j], op),
                    calculate(max_vals[i][k], min_vals[k + 1][j], op),
                    calculate(min_vals[i][k], max_vals[k + 1][j], op),
                    calculate(min_vals[i][k], min_vals[k + 1][j], op),
                ]
                
                # Оновлюємо максимальне та мінімальне значення для підвиразу [i:j]
                max_vals[i][j] = max(max_vals[i][j], *possible_values)
                min_vals[i][j] = min(min_vals[i][j], *possible_values)

    # Повертаємо максимальне значення для всього виразу
    return max_vals[0][n - 1]

# Введення виразу
expression = "5-3*10+2-"
max_result = maximize_expression(expression)

print(f"Вираз: {expression}")
print(f"Максимальне значення: {max_result}")
