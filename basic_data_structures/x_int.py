print('Арифметические операторы:')
print("Сложение целых чисел:                                    2 + 2 = {result}"   .format(result = 2 + 2))
print("Вычитание целых чисел:                                   2 - 2 = {result}"   .format(result = 2 - 2))
print("Умножение целых чисел:                                   2 * 2 = {result}"   .format(result = 2 * 2))
print("Деление целых чисел:                                     2 / 2 = {result}"   .format(result = int(2 / 2)))
print("Модуль четного числа:                                    2 % 2 = {result}"   .format(result = 2 % 2))
print("Модуль нечетного числа:                                  3 % 2 = {result}"   .format(result = 3 % 2))
print("Деление с остатком целых чисел:                          2 // 2 = {result}"  .format(result = 2 // 2))
print("Возвращает пару частное-остаток от деления аргументов:   2 / 2 = {result}"   .format(result = divmod(2, 2)))
print("Возведение в степень:                                    2 ^ 2 = {result}"   .format(result = pow(2, 2)))
print("Получение корня числа:                                   4 ** 2 = {result}"  .format(result = int(2 ** (1 / 2))))
print("* — операторы присваивания работают аналогичным образом.")

print('\nПобитовые операторы:')
print("Двоичное AND:            5 & 2 = {result}"   .format(result = 5 & 2))
print("Двоичное OR:             5 | 2 = {result}"   .format(result = 5 | 2))
print("Двоичное XOR:            5 ^ 2 = {result}"   .format(result = 5 ^ 2))
print("Двоичное дополнение:     ~2 = {result}"      .format(result = ~2))
print("Двоичное сдвиг влево:    5 << 2 = {result}"  .format(result = 5 << 2))
print("Двоичное сдвиг вправо:   5 >> 2 = {result}"  .format(result = 5 >> 2))

print('\nОператоры сравнения:')
print("Сравнение целых чисел: 5 == 2: {result}"     .format(result = 5 == 2))
print("Сравнение целых чисел: 5 != 2: {result}"     .format(result = 5 != 2))
print("Сравнение целых чисел: 5 < 2:  {result}"     .format(result = 5 < 2))
print("Сравнение целых чисел: 5 > 2:  {result}"     .format(result = 5 > 2))
print("Сравнение целых чисел: 5 <= 2: {result}"     .format(result = 5 <= 2))
print("Сравнение целых чисел: 5 >= 2: {result}"     .format(result = 5 >= 2))

print('\nЛогические операторы:')
print("Логическое И:    5 == 2 И 5 != 2:        {result}"     .format(result = 5 == 2 and 5 != 2))
print("Логическое !:    ! (5 == 2 И 5 != 2):    {result}"     .format(result = not (5 == 2 and 5 != 2)))
print("Логическое ИЛИ:  5 == 2 ИЛИ 5 != 2:      {result}"     .format(result = 5 == 2 or 5 != 2))

print('\nОператоры членства:')
print("Определяет, (IN) входит ли число 2 в список: 1, 2, 3, 4: {result}"       .format(result = 2 in [1, 2, 3, 4]))
print("Определяет, (NOT IN) входит ли число 2 в список: 1, 2, 3, 4: {result}"   .format(result = 2 not in [1, 2, 3, 4]))

print('\nОператоры идентификации (Сравнивает id объектов):')
print("Сравнивает id объектов (IS): 2 is 2: {result}"       .format(result = 2 is 2))
print("Сравнивает id объектов (IS NOT): 2 is 2: {result}"   .format(result = 2 is not 2))

print('\nДругие операции:')
print("bit_length — выводит длину числа 5 в бинарном виде: {value} = {result}".format(value = bin(5), result = (5).bit_length()))
print("Округление числа: 0.75 = {result}".format(result = round(0.75)))