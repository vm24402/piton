from datetime import datetime
print(datetime.now())  # Выводит текущую дату и время

#1
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения функции {func.__name__}: {execution_time} секунд")
        return result

    return wrapper


@timing_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")


if __name__ == "__main__":
    fibonacci()

#2
def read_file(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            data = file.read()

            if not data:
                raise Exception("файл пустой")

            print(f"Содержимое файла:\n{data}")
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


read_file("filename.txt")

#3
def add_two_numbers():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)
        result = 2 + number
        print("Результат сложения:", result)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == "__main__":
    try:
        add_two_numbers()
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")

#4
import functools


# Создаем декоратор log_args для логирования аргументов функции
def log_args(func):
    @functools.wraps(func)  # Сохраняем метаданные функции
    def wrapper(*args, **kwargs):
        # Собираем строковое представление позиционных аргументов
        arg_str = ", ".join([repr(arg) for arg in args])
        # Собираем строковое представление именованных аргументов
        kwarg_str = ", ".join([f"{k}={v!r}" for k, v in kwargs.items()])

        # Объединяем строки, если оба типа аргументов присутствуют
        if arg_str and kwarg_str:
            arg_str += ", " + kwarg_str
        elif kwarg_str:
            arg_str = kwarg_str

        # Выводим информацию о вызове функции с аргументами
        print(f"Вызов функции {func.__name__}({arg_str})")

        # Вызываем исходную функцию и сохраняем результат
        result = func(*args, **kwargs)

        # Возвращаем результат выполнения функции
        return result

    # Возвращаем обернутую функцию
    return wrapper


# Применяем декоратор log_args к функции add
@log_args
def add(a, b):
    return a + b


# Применяем декоратор log_args к функции greet
@log_args
def greet(name):
    return f"Привет, {name}!"


if __name__ == "__main__":
    # Вызываем функцию add с аргументами 2 и 3
    result1 = add(2, 3)

    # Вызываем функцию greet с аргументом "Alice"
    result2 = greet("Alice")

#5
# Создаем пользовательское исключение CustomException,
# которое будет использоваться для обработки специфических ошибок.
class CustomException(Exception):
    def __init__(self, message="Произошла ошибка"):
        self.message = message
        super().__init__(self.message)

# Функция divide(a, b) выполняет деление двух чисел a на b.
# Если b равно 0, то возбуждается исключение CustomException с сообщением "Деление на ноль недопустимо".
# В противном случае возвращается результат деления a на b.
def divide(a, b):
    if b == 0:
        raise CustomException("Деление на ноль недопустимо")
    return a / b

# Функция process_data(data) принимает входные данные data
# и выполняет какую-либо обработку. Если data пусто, то
# возбуждается исключение CustomException с сообщением "Пустые данные недопустимы".
# В противном случае возвращается сообщение об успешной обработке данных.
def process_data(data):
    if not data:
        raise CustomException("Пустые данные недопустимы")
    return "Данные обработаны успешно"

# Основной блок кода, выполняемый при запуске скрипта.
if __name__ == "__main__":
    try:
        result = divide(10, 0)  # Попытка деления на ноль.
    except CustomException as e:
        print(f"Ошибка: {e}")  # Вывод сообщения об ошибке CustomException.
    else:
        print(f"Результат: {result}")  # Вывод результата деления (не выполнится, так как возникла ошибка).

    try:
        result = process_data([])  # Попытка обработки пустых данных.
    except CustomException as e:
        print(f"Ошибка: {e}")  # Вывод сообщения об ошибке CustomException.
    else:
        print(f"Результат: {result}")  # Вывод сообщения об успешной обработке данных (не выполнится, так как возникла ошибка).