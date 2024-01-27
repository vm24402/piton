# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
- Михеев Владислав Вячеславович
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.

```python
if __name__ == "__main__":
    input_data = input("Введите последовательность чисел, разделенных пробелом: ")
    numbers_list = input_data.split()
    numbers_tuple = tuple(map(int, numbers_list))
    print("Список чисел:", numbers_list)
    print("Кортеж чисел:", numbers_tuple)
```

### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-6/pic/Screenshot_1.jpg)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print("Список чисел:", numbers_list)`: Выводит список чисел.

2. `print("Кортеж чисел:", numbers_tuple)`: Выводит кортеж чисел.

## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).

```python
def process_tuple(tup, element):
    if element in tup:
        index = tup.index(element)
        new_tup = tup[:index] + tup[index + 1:]
        return new_tup
    else:
        return tup


if __name__ == "__main__":
    print(process_tuple(tuple(map(int, input("Введите кортеж: ").split())), int(input("Введите число: "))))
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-6/pic/Screenshot_2.jpg)

## Выводы

В данном коде выводит одну строку с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(process_tuple(tuple(map(int, input("Введите кортеж: ").split())), int(input("Введите число: "))))`: Выводит измененный результат, без числа, введенного на клавиатуре, либо выводит без изменений, если данного числа нет в кортеже.

## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайтефункцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.

```python
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
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-6/pic/Screenshot_3.jpg)

## Выводы

В данном коде выводит одну строку с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(count_most_common_numbers(input("Введите строку: ")))`: Выводит количество повторений чисел в строке.

## Самостоятельная работа №4
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.

```python
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
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-6/pic/Screenshot_4.jpg)

## Выводы

В данном коде выводит одну строку с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(find_employee_movement(tuple(map(int, input("Введите кортеж: ").split())),`: Выводит новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно, если элемента нет - выводит пустой кортеж.
  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.Напишите функцию, которая будет принимать список слов и возвращать кортеж, содержащий два элемента: 1. Количество гласных букв (A, E, I, O, U) в каждом слове. 2. Словарь, в котором ключи - это гласные буквы, а значения - количество раз, которое каждая из гласных букв встречается во всех словах в списке.

```python
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
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-6/pic/Screenshot_5.jpg)

## Выводы

В данном коде выводятся три строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(result1)`: Выводит первый результат.

2. `print(result2)`: Выводит второй результат.

3. `print(result3)`: Выводит третий результат.