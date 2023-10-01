def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count

def replace_ugly(sentence):
    return sentence.replace("ugly", "beauty")

def check_start_end(sentence):
    return sentence.startswith("The") and sentence.endswith("end")

sentences = []

for i in range(3):
    sentence = input("Введите предложение на английском: ")
    sentences.append(sentence)

for sentence in sentences:
    print("Длина предложения:", len(sentence))
    print("Предложение в нижнем регистре:", sentence.lower())
    print("Количество гласных:", count_vowels(sentence))
    print("Заменённые слова:", replace_ugly(sentence))
    print("Начинается с 'The' и заканчивается на 'end':", check_start_end(sentence))
    print()