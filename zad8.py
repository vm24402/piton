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