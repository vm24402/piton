# 1
if __name__ == "__main__":
    input_data = input("Введите последовательность чисел, разделенных пробелом: ")
    numbers_list = input_data.split()
    numbers_tuple = tuple(map(int, numbers_list))
    print("Список чисел:", numbers_list)
    print("Кортеж чисел:", numbers_tuple)


# 2
def process_tuple(tup, element):
    if element in tup:
        index = tup.index(element)
        new_tup = tup[:index] + tup[index + 1:]
        return new_tup
    else:
        return tup


if __name__ == "__main__":
    print(process_tuple(tuple(map(int, input("Введите кортеж: ").split())), int(input("Введите число: "))))


# 3
def count_most_common_numbers(input_string):
    digit_count = {}

    for char in input_string:
        if char.isdigit():
            digit = int(char)
            digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digit_count = sorted(digit_count.items(), key=lambda x: x[1], reverse=True)
    most_common_numbers = sorted_digit_count[:3]
    most_common_numbers = sorted(most_common_numbers, key=lambda x: x[0])

    result_dict = {num: count for num, count in most_common_numbers}

    return result_dict


if __name__ == "__main__":
    print(count_most_common_numbers(input("Введите строку: ")))


# 4
def find_employee_movement(log, employee_id):
    start_idx = log.index(employee_id) if employee_id in log else -1
    if start_idx == -1:
        return ()

    end_idx = log[start_idx + 1:].index(employee_id) if employee_id in log[start_idx + 1:] else -1
    if end_idx == -1:
        return log[start_idx:]

    end_idx += start_idx + 1

    return log[start_idx:end_idx + 1]


if __name__ == "__main__":
    print(find_employee_movement(tuple(map(int, input("Введите кортеж: ").split())),
                                 int(input("Введите ID сотрудника: "))))

# 5
"""
Напишите функцию, которая будет принимать список слов и возвращать кортеж, содержащий два элемента:
1. Количество гласных букв (A, E, I, O, U) в каждом слове.
2. Словарь, в котором ключи - это гласные буквы, а значения - количество раз, которое каждая из гласных букв встречается во всех словах в списке.
"""
def count_vowels_in_words(word_list):
    vowels = "AEIOUaeiou"
    vowel_counts = []
    vowel_occurrences = {}

    for word in word_list:
        vowel_count = sum(1 for letter in word if letter.lower() in vowels)
        vowel_counts.append(vowel_count)

        for letter in word:
            if letter in vowels:
                if letter in vowel_occurrences:
                    vowel_occurrences[letter] += 1
                else:
                    vowel_occurrences[letter] = 1

    return tuple(vowel_counts), vowel_occurrences


word_list1 = ["apple", "banana", "cherry"]
result1 = count_vowels_in_words(word_list1)
print(result1)

word_list2 = ["hello", "world"]
result2 = count_vowels_in_words(word_list2)
print(result2)

word_list3 = ["programming", "is", "fun"]
result3 = count_vowels_in_words(word_list3)
print(result3)