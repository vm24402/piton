from datetime import datetime
print(datetime.now())  # Выводит текущую дату и время

# 1
arr = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
       1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
       5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
       5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
       3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506
       ]

employee_visits = {}
for check in arr:
    if check in employee_visits:
        employee_visits[check] += 1
    else:
        employee_visits[check] = 1

most_frequent_employee = max(employee_visits, key=employee_visits.get)

print(f"Сколько было выдано чеков: {len(arr)}")
print(f"Сколько разных людей посетило ресторан: {len(set(arr))}")
print(f"Работник с кодом {most_frequent_employee} посетил ресторан {employee_visits[most_frequent_employee]} раз(а).")

# 2
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6,
           26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3,
           18.7, 31.9, 12.9, 37.4
           ]

results.sort()

print("Три лучших результата:", results[:3])
print("Три худших результата:", results[-3:])
print("Все результаты начиная с 10-го:", results[9:])

# 3
import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max1, min1 = max(one), min(one)
max2, min2 = max(two), min(two)
max3, min3 = max(three), min(three)

minP = (min1 + min2 + min3) / 2
maxP = (max1 + max2 + max3) / 2

minS = math.sqrt(minP * (minP - min1) * (minP - min2) * (minP - min3))
maxS = math.sqrt(maxP * (maxP - max1) * (maxP - max2) * (maxP - max3))

print("Вычисленная площадь треугольника, длинами сторон которого являются минимальные значения списков, равна: ", minS)
print("Вычисленная площадь треугольника, длинами сторон которого являются максимальные значения списков, равна: ", maxS)

# 4
def process_grades(grades):
    updated_grades = []

    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            updated_grades.append(4)
        else:
            updated_grades.append(grade)

    return updated_grades


grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

updated_grades1 = process_grades(grades1)
updated_grades2 = process_grades(grades2)
updated_grades3 = process_grades(grades3)

print("Обновленные оценки (список 1):", updated_grades1)
print("Обновленные оценки (список 2):", updated_grades2)
print("Обновленные оценки (список 3):", updated_grades3)


# 5
def transform(input_list):
    result_set = set()

    for num in input_list:
        num_str = str(num)
        num_count = input_list.count(num)

        if num_count > 1:
            result_set.add(num_str * num_count)

        result_set.add(num)

    return result_set


list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

result_set_1 = transform(list1)
result_set_2 = transform(list2)
result_set_3 = transform(list3)

print(result_set_1)
print(result_set_2)
print(result_set_3)