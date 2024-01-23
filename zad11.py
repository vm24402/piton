from datetime import datetime
print(datetime.now())  # Выводит текущую дату и время

def fib(n):
    a, b = 1, 1
    count = 0

    with open("fib.txt", "w") as file:
        while count < n:
            yield a
            file.write(str(a) + '\n')

            a, b = b, a + b
            count += 1


if __name__ == "__main__":
    count_numbers = 200
    fib_sequence = list(fib(count_numbers))
    print(f"The {count_numbers}th Fibonacci number is: {fib_sequence[-1]}")