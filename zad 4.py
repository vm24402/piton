# 4
sentence = input("Введите строку: ")
print("Длина:", len(sentence))
print("Нижний регистр:", sentence.lower())
print("Гласных:", sum(1 for letter in sentence if letter in ['a', 'e', 'i', 'o', 'u']))
print("Замененная строка:", sentence.replace("ugly", "beauty"))
print("Строка начинается со 'The':", sentence.startswith("The"))
print("Строка начинается со 'end':", sentence.endswith("end"))