# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
import re
from collections import Counter


def find_count_words(text):
    words = re.findall(r'\w+', text.lower())
    return words


def find_most_common_word(words):
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)
    return most_common_word[0] if most_common_word else None


if __name__ == "__main__":
    with open('./input.txt', 'r', encoding='utf-8') as file:
        article_text = file.read()

    article_words = find_count_words(article_text)
    most_common = find_most_common_word(article_words)

    total_words = f"Общее количество слов в статье: {len(article_words)}"
    common_word = f"Самое часто встречающееся слово: '{most_common[0]}' (встречается {most_common[1]} раз)" if most_common else "Статья не содержит слов."

    print(total_words)
    print(common_word)

    with open('./result.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(total_words + "\n")
        result_file.write(common_word + "\n")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-7/pic/Screenshot_1.jpg)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(total_words)`: Выводит количество слов в статье.

2. `print(common_word)`: Выводит часто встречающееся слово.

## Результаты работы кода можно посмотреть в папке pic, там прикреплены файлы.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
import os
import json


def input_expense():
    return {
        "name": input("Введите название расхода: "),
        "amount": float(input("Введите сумму расхода: ")),
        "date": input("Введите дату расхода (дд-мм-гггг): ")
    }


def save_expenses(expenses, file):
    with open(file, "w") as expenses_file:
        json.dump(expenses, expenses_file)


def load_expenses(file):
    if os.path.exists(file):
        with open(file, "r") as expenses_file:
            return json.load(expenses_file)
    else:
        return []


def main():
    expenses_file = "expenses.json"
    expenses = load_expenses(expenses_file)

    while True:
        print("\nВыберите действие:")
        print("1. Ввести новый расход")
        print("2. Показать все расходы")
        print("3. Выйти")

        match int(input("Введите номер действия: ")):
            case 1:
                new_expense = input_expense()
                expenses.append(new_expense)
                save_expenses(expenses, expenses_file)
                print("Расход успешно добавлен!")
            case 2:
                if expenses:
                    print("\nСписок всех расходов:")
                    for expense in expenses:
                        print(f"Имя: {expense['name']}, Сумма: {expense['amount']}, Дата: {expense['date']}")
                else:
                    print("Список расходов пуст.")
            case 3:
                break
            case _:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-7/pic/Screenshot_2.jpg)

## Выводы

В данном коде выводятся четыре строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print("\nВыберите действие:")`: Выводит возможные варианты для выбора действия.

2. `print("1. Ввести новый расход")`: Вводит новый расход.

3. `print("2. Показать все расходы")`: Показывает все введеные расходы.

4. `print("3. Выйти")`: Выходит из программы.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
with open('.\\input (1).txt', 'r') as file:
    text = file.read()

letter_count = len([char for char in text if char.isalpha()])
word_count = len(text.split())
line_count = text.count('\n') + 1  # добавляем 1, так как последняя строка не завершается символом новой строки

print("Input file contains:")
print(f"{letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-7/pic/Screenshot_3.jpg)

## Выводы

В данном коде выводятся четыре строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print("Input file contains:")`: Выводит статистику файла.

2. `print(f"{letter_count} letters")`: Выводит количество букв.

3. `print(f"{word_count} words")`: Выводит количество слов.

4. `print(f"{line_count} lines")`: Выводит количество строк.
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, 

```python
import re


def load_prohibited_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words


def multiple_replace(target_str, bad_words):
    for word in bad_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        target_str = pattern.sub("*" * len(word), target_str)
    return target_str


if __name__ == "__main__":
    output_sentence = multiple_replace(input("Enter a sentence: "), load_prohibited_words(".\\input (2).txt"))
    print(f"Modified sentence:\n{output_sentence}")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-7/pic/Screenshot_4.jpg)

## Выводы

В данном коде выводится одна строка с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(f"Modified sentence:\n{output_sentence}")`: Выводит измененный текст, учитывая запрещенные слова.
  
## Самостоятельная работа №5
### Анализ текстовых данных: поиск наиболее часто встречающихся слов и фраз в большом текстовом файле.

```python
from collections import Counter
import re


if __name__ == "__main__":
    with open(".\\large_text.txt", "r", encoding="utf-8") as file:
        text = file.read()
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)

        word_counts = Counter(words)
        most_common_words = word_counts.most_common(10)

        phrases = re.findall(r'\b\w+\s\w+\b', text)
        phrase_counts = Counter(phrases)
        most_common_phrases = phrase_counts.most_common(10)

    print("Наиболее часто встречающиеся слова:")
    for word, count in most_common_words:
        print(f"{word}: {count} раз")

    print("\nНаиболее часто встречающиеся фразы:")
    for phrase, count in most_common_phrases:
        print(f"{phrase}: {count} раз")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-7/pic/Screenshot_5.jpg)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(f"{word}: {count} раз")`: Выводит часто встречающиеся слова.

2. `print(f"{phrase}: {count} раз")`: Выводит часто встречающиеся фразы.

  