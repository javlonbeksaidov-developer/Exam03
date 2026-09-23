"""11. "Student" nomli klass yarating. Unda ism va yosh atributlari, hamda ma'lumotlarni chop etadigan metod bo'lsin."""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"
