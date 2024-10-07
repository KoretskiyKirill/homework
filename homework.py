import math
try:
    #1
    num = int(input('введите число'))
    if num % 2 == 0 and num % 4 == 0:
        print('чётно и кратно четырём')
    else:
        print('не чётно или не кратно четырём')
    #2
    num = int(input('введите число'))
    if num % 2 != 0 and num % 5 == 0:
        print('не чётно и кратно пяти')
    else:
        print('чётно или не кратно пяти')
    #3
    num = int(input('введите число'))
    if num % 2 != 0 and num % 7 == 0:
        print('не чётно и кратно семи')
    else:
        print('чётно или не кратно семи')
    #4
    num = int(input('введите число'))
    if num % 2 == 0 and num % 10 == 0:
        print('чётно и кратно десяти')
    else:
        print('не чётно или не кратно десяти')
    #5
    length_1 = int(input('введите длину коробки'))
    width_1 = int(input('введите ширину коробки'))
    height = int(input('введите высоту коробки'))
    length_2 = int(input('введите длину двери'))
    width_2 = int(input('введите ширину двери'))
    door = length_2 * width_2
    if length_1 * width_1 <= door or width_1 * height <= door or length_1 * height <= door:
        print('проходит')
    else:
        print('не проходит')
except(ValueError):
    print('ЧИСЛО!!!!')
    #6
try:
    num = float(input('введите число'))
    if num < 0:
        print('отрицательное')
    elif num > 0:
        print('положительное')
    else:
        print('0')
    #7
    d = float(input('введите число'))
    a = float(input('введите число'))
    if (a**2)*2 == d:
        print('можно')
    else:
        print('нельзя')
    #8
    s = float(input('введите число'))
    k = float(input('введите число'))
    r = float(input('введите число'))
    if (s ** 0.5) - k >= r:
        print('войдёт')
    else:
        print('не войдёт')
    #9
    up_down = ''
    seat = int(input('номер места'))
    if seat % 2 == 0:
        up_down = 'верхнее'
    else:
        up_down = 'нижнее'
    if seat < 37:
        print(up_down, 'купейное')
    else:
        print(up_down, 'боковое')
    #10
    num = int(input('введите число'))
    d_500 = num // 500
    d_100 = num // 10
    d_10 = num // 10
    d_2 = num // 2
    if num % 2 == 0:
        print(d_500,d_100,d_10,d_2)
    else:
        print('erorr')
    #11
    A = int(input('сторона банки'))
    r = int(input('радиус банки'))
    h = int(input('высота банки'))
    m = int(input('кол-во жидкости'))
    if A **3>=m:
        print('да')
    else:
        print('нет')
    if r *2*h*math.pi>=m:
        print('да')
    else:
        print('нет')
    if A**3+r*2*h *math.pi>=m:
        print('да')
    else:
        print('нет')
except(ValueError):
    print('число')
try:
    # 13. Проверка существования треугольника и его тип
    X = float(input("Введите длину стороны X: "))
    Y = float(input("Введите длину стороны Y: "))
    Z = float(input("Введите длину стороны Z: "))
    if (X + Y > Z) and (X + Z > Y) and (Y + Z > X):
        print("Треугольник существует.")    # Проверка прямоугольного треугольника по теореме Пифагора
        if (X**2 + Y**2 == Z**2) or (X**2 + Z**2 == Y**2) or (Y**2 + Z**2 == X**2):        print("Треугольник прямоугольный.")
        else:        print("Треугольник не является прямоугольным.")
    else:    print("Треугольник не существует.")

    # 14. Проверка принадлежности числа заданному промежутку [a, b]a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    X = float(input("Введите число X: "))
    a = float(input("Введите a: "))
    if a <= X <= b:
        print(f"Число {X} принадлежит промежутку [{a}, {b}].")
    else:
        print(f"Число {X} не принадлежит промежутку [{a}, {b}].")
    # 15. Вычисление значения функции Z = 1 / (XY)
    X = float(input("Введите число X: "))
    Y = float(input("Введите число Y: "))
    if X != 0 and Y != 0:  # Проверяем, чтобы X и Y не были нулевыми
        Z = 1 / (X * Y)
        print(f"Значение функции Z = 1 / (XY) равно: {Z:.2f}")
    else:    print("X и Y не могут быть нулевыми.")

    # 16. Проверка выполнения неравенств A < B >= CA = float(input("Введите A: "))
    B = float(input("Введите B: "))
    C = float(input("Введите C: "))
    A = float(input("Введите A: "))
    if A < B and B >= C:
        print("Условие A < B >= C выполняется.")
    elif A < B:
        print("Выполняется неравенство A < B.")
    elif B >= C:
        print("Выполняется неравенство B >= C.")
    else:
        print("Никакое из неравенств не выполняется.")
    # 17. Проверка, может ли прямоугольник со сторонами a,b уместиться внутри прямоугольника со сторонами c,d
    a = float(input("Введите сторону a внутреннего прямоугольника: "))
    b = float(input("Введите сторону b внутреннего прямоугольника: "))
    c = float(input("Введите сторону c внешнего прямоугольника: "))
    d = float(input("Введите сторону d внешнего прямоугольника: "))
    if (a <= c and b <= d) or (a <= d and b <= c):
        print("Прямоугольник со сторонами a и b помещается внутри прямоугольника со сторонами c и d.")
    else:
        print("Прямоугольник со сторонами a и b не помещается внутри.")
except(ValueError):
    print('число')
try:
    # 1. Выводим числа от 1 до 20
    for i in range(1, 21):
        print(i)

    # 2. Числа от 1001 до 1025 с шагом 3
    for i in range(1001, 1026, 3):
        print(i)

    # 3. Числа от 100 до 0 с шагом -4
    for i in range(100, 0, -4):
        print(i)

    # 4. Числа от 1.2 до 2.8 с шагом 0.2
    for i in range(12, 29, 2):
        print(i / 10)

    # 5. Печатаем заданные строки
    for i in range(25, 36):
        print(f"{i} {i + 0.5} {i - 0.2}")

    # 6. Таблица цен на доллары
    dollar_to_rub = float(input("Введите курс доллара в рублях: "))
    print("USD\tRUB\tKG")
    for dollar in range(1, 101):
        rub = dollar * dollar_to_rub
        kg = rub / 20
        print(f"{dollar}\t{rub:.2f}\t{kg:.2f}")

    # 7. Сумма от 1 до n
    n = int(input("Введите n: "))
    total_sum = sum(range(1, n + 1))
    print(total_sum)

    # 8. Сумма от 10 до 88
    total_sum = sum(range(10, 89))
    print(total_sum)

    # 9. Произведение от 5 до 13
    product = 1
    for i in range(5, 14):
        product *= i
    print(product)

    # 10. Сумма 1 + 4 + 7 + ... + 112
    total_sum = sum(range(1, 113, 3))
    print(total_sum)

    # 11. Сумма косинусов
    import math

    total_sum = sum(math.cos(math.radians(i)) for i in range(35, 112, 22))
    print(total_sum)

    # 12. Сумма от 23 до 910 с шагом 11
    total_sum = sum(range(23, 911, 11))
    print(total_sum)
    1
    # 13. Суммы от 1 до n — 100 строк
    for n in range(1, 101):
        total_sum = sum(range(1, n + 1))
        print(total_sum)

    # 14. Сумма квадратов первых n натуральных чисел
    n = int(input("Введите n для суммы квадратов: "))
    total_sum = sum(i ** 2 for i in range(1, n + 1))
    print(total_sum)

    # 15. Сумма от 1 + 12 + 13 + ... + 1n
    n = int(input("Введите n для суммы с 1 + 12 + 13 + ...: "))
    total_sum = sum(n + 1 for n in range(1, n + 1))
    print(total_sum)

    # 16. p=(a+1)^2 * (a+2)^2 * ... * (a+n)^2
    a = int(input("Введите a: "))
    n = int(input("Введите n: "))
    product = 1
    for i in range(1, n + 1):
        product *= (a + i) ** 2
    print(product)

    # 17. Сумма 1/cos(x) + 1/cos(x^2) + ... + 1/cos(x^n)
    x = float(input("Введите x: "))
    n = int(input("Введите n: "))
    total_sum = sum(1 / math.cos(x ** i) for i in range(1, n + 1))
    print(total_sum)

    # 18. Сумма 1⋅2 + 2⋅3⋅4 + ... + n⋅(n+1)⋅...⋅2n
    n = int(input("Введите n для суммы 1⋅2 + ...: "))
    total_sum = sum(i * (i + 1) for i in range(1, n + 1))
    print(total_sum)

    # 19. Пробег лыжника по дням
    distance = 10
    for day in range(1, 11):
        print(f"День {day}: {distance:.2f} км")
        distance *= 1.1

    # Суммарный путь за первые 7 дней
    total_distance = 0
    distance = 10
    for day in range(1, 8):
        total_distance += distance
        distance *= 1.1
    print(f"Суммарный путь за 7 дней: {total_distance:.2f} км")

    # Суммарный путь за n дней
    n = int(input("Введите количество дней для суммарного пути: "))
    total_distance = 0
    distance = 10
    for day in range(1, n + 1):
        total_distance += distance
        distance *= 1.1
    print(f"Суммарный путь за {n} дней: {total_distance:.2f} км")

    # Когда прекратить увеличивать пробег
    distance = 10
    day = 1
    while distance <= 80:
        distance *= 1.1
        day += 1
    print(f"Перестаньте увеличивать пробег на день {day}.")

    # 20. Числа от 1000 до 9999 с различными цифрами
    for number in range(1000, 10000):
        str_number = str(number)
        if len(set(str_number)) == len(str_number):
            print(number)

    # 21. Числа от 1000 до 9999 без 5 и 6
    for number in range(1000, 10000):
        if '5' not in str(number) and '6' not in str(number):
            print(number)

    # 22. Пятизначные числа с заданными свойствами
    for number in range(10000, 100000):
        digits = [int(d) for d in str(number)]
        if (number % 2 == 0) and (digits[2] % 2 == 1) and (sum(digits) % 4 == 0):
            print(number)

    # 23. Числа от 1000 до 9999 с цифрой 3

    for number in range(1000, 10000):
        if '3' in str(number):
            print(number)

    # 24. Трехзначные числа = сумме кубов своих цифр
    for number in range(100, 1000):
        digits = [int(d) for d in str(number)]
        if number == sum(d ** 3 for d in digits):
            print(number)

    # 25. Четырехзначные числа, которые в 600 раз больше суммы своих цифр
    count = 0
    for number in range(1000, 10000):
        digits_sum = sum(int(d) for d in str(number))
        if number == 600 * digits_sum:
            count += 1
    print(count)

    # 26. Число, которое делится на 11, остаток 1 при делении на 2..10
    for number in range(11, 1000000, 11):
        if all(number % i == 1 for i in range(2, 11)):
            print(number)
            break

    # 27. Вывод n единиц, 2n двоек, 3n троек
    n = int(input("Введите n для вывода единиц и двоек: "))
    for i in range(1, 4):
        print(f"{i} " * (i * n))

    # 28. Десять десяток, девять девяток, ... , одну единицу
    total_sum = 0
    for i in range(10, 0, -1):
        total_sum += i * (10 - i + 1)
        print(f"{i} " * (10 - i + 1))
    print("Сумма:", total_sum)
except(ValueError):
    print('число')