def calculate(a, b, operation):
    if operation == '1':
        return a + b, '+'
    elif operation == '2':
        return a - b, '-'
    elif operation == '3':
        return a * b, '*'
    elif operation == '4':
        if b == 0:
            return None, '/'
        return a / b, '/'
    return None, None


def save_history(a, b, symbol, result):
    with open('calculations.txt', 'a', encoding='utf-8') as f:
        f.write(f'Результат: {a} {symbol} {b} = {result}\n')


def show_history():
    try:
        with open('calculations.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('История вычислений пуста.')
        return

    print('История вычислений:')
    if not lines:
        print('История вычислений пуста.')
    else:
        for line in lines:
            print(line.rstrip())


print('Выберите операцию:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Просмотр истории вычислений')

choice = input('Введите номер операции (1-5): ')

if choice == '5':
    show_history()
else:
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
    except ValueError:
        print('Ошибка: введите корректные числа.')
        exit()

    result, symbol = calculate(a, b, choice)

    if result is None and symbol is None:
        print('Ошибка: неверный номер операции.')
    elif result is None and symbol == '/':
        print('Ошибка: деление на ноль.')
    else:
        # деление выводим с двумя знаками после запятой, как в примере
        if choice == '4':
            print(f'Результат: {a:g} / {b:g} = {result:.2f}')
            save_history(a, b, symbol, f'{result:.2f}')
        else:
            print(f'Результат: {a:g} {symbol} {b:g} = {result:g}')
            save_history(a, b, symbol, f'{result:g}')

