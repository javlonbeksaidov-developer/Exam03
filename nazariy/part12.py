"""12. Yaratilgan "Student" klassidan foydalanib 2 ta turli obyekt hosil qiling va ularning ma'lumotlarini ekranga chiqaring."""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


javlon = Student("javlon", 21)
yashnar = Student("yashnar", 21)