# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
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
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Polina", 21)
print(person1.introduce())
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-8/pic/Screenshot_1.jpg)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(person1.introduce())`: Выводит имя и возраст.
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} added {friend.name} as a friend.")


person2 = Person("Polina", 25)
person3 = Person("Denis", 28)

person2.introduce()
person3.introduce()

person2.add_friend(person3)
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-8/pic/Screenshot_1.jpg)

## Выводы

В данном коде выводятся две строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(f"Hi, my name is {self.name} and I am {self.age} years old.")`: Выводит в строку первый текст.

2. `print(f"{self.name} added {friend.name} as a friend.")`: Выводит в строку второй текст.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
cclass Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} added {friend.name} as a friend.")


person2 = Person("Vlad", 32)
person3 = Person("Oleg", 45)

person2.introduce()
person3.introduce()

person2.add_friend(person3)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} with ID {self.student_id} is studying {subject}.")


student1 = Student("georgiy", 22, "S12345")
student1.study("Mathematics")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-8/pic/Screenshot_1.jpg)
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} added {friend.name} as a friend.")


person2 = Person("Polina", 25)
person3 = Person("Denis", 28)

person2.introduce()
person3.introduce()

person2.add_friend(person3)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} with ID {self.student_id} is studying {subject}.")


student1 = Student("Eva", 22, "S12345")
student1.study("Mathematics")
class PrivatePerson(Person):
    def __init__(self, name, age, ssn):
        super().__init__(name, age)
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if len(new_ssn) == 9:
            self.__ssn = new_ssn
            print(f"{self.name}'s SSN has been updated.")
        else:
            print("Invalid SSN format. SSN should be 9 digits.")


private_person = PrivatePerson("Svetlana", 99, "123456789")
print(f"{private_person.name}'s SSN: {private_person.get_ssn()}")
private_person.set_ssn("987654321")
print(f"{private_person.name}'s Updated SSN: {private_person.get_ssn()}")
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-8/pic/Screenshot_1.jpg)
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f"{self.name} added {friend.name} as a friend.")


person2 = Person("Polina", 25)
person3 = Person("Denis", 28)

person2.introduce()
person3.introduce()

person2.add_friend(person3)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} with ID {self.student_id} is studying {subject}.")


student1 = Student("georgiy", 22, "S12345")
student1.study("Mathematics")
class PrivatePerson(Person):
    def __init__(self, name, age, ssn):
        super().__init__(name, age)
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, new_ssn):
        if len(new_ssn) == 9:
            self.__ssn = new_ssn
            print(f"{self.name}'s SSN has been updated.")
        else:
            print("Invalid SSN format. SSN should be 9 digits.")


private_person = PrivatePerson("Svetlana", 99, "123456789")
print(f"{private_person.name}'s SSN: {private_person.get_ssn()}")
private_person.set_ssn("987654321")
print(f"{private_person.name}'s Updated SSN: {private_person.get_ssn()}")
def introduce_people(people):
    for person in people:
        person.introduce()


people_to_introduce = [person2, person3, student1, private_person]
introduce_people(people_to_introduce)
```
### Результат.
![Меню](https://github.com/vm24402/piton/blob/%D1%82%D0%B5%D0%BC%D0%B0-8/pic/Screenshot_1.jpg)
