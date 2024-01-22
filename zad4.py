# 1
# Импортируем класс datetime из модуля datetime
from datetime import datetime

# Импортируем функцию sqrt из модуля math
from math import sqrt

def main(**kwargs):
    """
    Рассчет result
    :param kwargs: входные ключи (в виде словаря)
    """
    # Перебираем ключи и значения в переданном словаре kwargs
    for key in kwargs.items():
        # Вычисляем результат: корень из суммы квадратов двух чисел в значениях словаря
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Выводим результат на экран
        print(result)


# Проверка, если имя текущего модуля равно 'main'
if __name__ == '__main__':
    # Засекаем текущее время
    start_time = datetime.now()

    # Вызываем функцию main с передачей ей словаря, в котором ключи - это строки,
    # а значения - это списки из двух чисел
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # Вычисляем время, прошедшее с начала выполнения программы
    time_costs = datetime.now() - start_time
    # Выводим на экран время выполнения программы
    print(f"Время выполнения программы - {time_costs}")

# 2
import random

def roll_dice():
    dice_value = random.randint(1, 6)

    print(f"Кубик: {dice_value}")

    if dice_value in [5, 6]:
        print("Вы победили")
    elif dice_value in [3, 4]:
        print("Вы продолжаете бросать кубик...")
        roll_dice()
    elif dice_value in [1, 2]:
        print("Вы проиграли")


# Точка входа в программу
if __name__ == "__main__":
    print("Игра в кости началась!")
    roll_dice()

# 3
import datetime
import time

duration = 5
start_time = datetime.datetime.now()

while True:
    current_time = datetime.datetime.now()

    print(current_time.strftime("%Y-%m-%d %H:%M:%S"))

    elapsed_time = current_time - start_time
    if elapsed_time.total_seconds() >= duration:
        break

    time.sleep(1)

# 4
def average(*args):
    if len(args) == 0:
        return 0
    else:
        total = sum(args)
        return total / len(args)

def main():
    # Пример вызова функции с разным количеством аргументов
    result1 = average(1, 2, 3, 4, 5)
    print(f"Среднее арифметическое: {result1}")

    result2 = average(10, 20, 30)
    print(f"Среднее арифметическое: {result2}")

    result3 = average()
    print(f"Среднее арифметическое: {result3}")

if __name__ == "__main__":
    main()

# 5
# file triangle_area.py
def calculate_triangle_area(a, b, c):
    # Полупериметр треугольника
    s = (a + b + c) / 2

    # Формула Герона для вычисления площади треугольника
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return area

# Пример использования функции (для тестирования)
# a, b, c = 5, 6, 7
# result = calculate_triangle_area(a, b, c)
# print(f"Площадь треугольника: {result}")


# file user_interaction.py
# from triangle_area import calculate_triangle_area

# Получаем длины сторон от пользователя
a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))

# Проверяем, можно ли построить треугольник с заданными сторонами
if a + b > c and a + c > b and b + c > a:
    # Вызываем функцию для вычисления площади треугольника
    result = calculate_triangle_area(a, b, c)
    print(f"Площадь треугольника: {result}")
else:
    print("С такими сторонами нельзя построить треугольник.")