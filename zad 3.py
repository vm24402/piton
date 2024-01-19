# 3
number = int(input("number = "))
if number < 0 or number > 10:
    print("Число должно быть от 1 до 10!")
else:
    if 0 <= number <= 3:
        print("Число от 0 до 3 включительно")
    elif 3 < number < 6:
        print("Число от 3 до 6")
    elif 6 <= number <= 10:
        print("Число от 6 до 10 включительно")