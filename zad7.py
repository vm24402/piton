
from datetime import datetime
print(datetime.now())  # Выводит текущую дату и время

#1
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

#2
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

#3
with open('./input.txt', 'r') as file:
    text = file.read()

letter_count = len([char for char in text if char.isalpha()])
word_count = len(text.split())
line_count = text.count('\n') + 1  # добавляем 1, так как последняя строка не завершается символом новой строки

print("Input file contains:")
print(f"{letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")

#4
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
    output_sentence = multiple_replace(input("Enter a sentence: "), load_prohibited_words("./input.txt"))
    print(f"Modified sentence:\n{output_sentence}")

#5
from collections import Counter
import re


if __name__ == "__main__":
    with open("./input2.txt", "r", encoding="utf-8") as file:
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