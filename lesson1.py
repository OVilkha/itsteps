from datetime import datetime
#new file#gofjejf
class Student:
    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} років, {self.height} cm"

    def __del__(self):
        print("Object deleted")

    def __bool__(self):
        return self.name != None

    def __len__(self):
        return self.height

    def get_info(self):
        year_now = datetime.now().year

first_student = Student("Петро", "Петренко", 15, 170)
print(first_student.name, first_student.surname, first_student.age, first_student.height)
print(f"Мене звати {first_student.name} {first_student.surname}. Мені {first_student.age}")
print(first_student)
second_student = Student()
print(second_student)
print(second_student.__bool__())
print(first_student.__bool__())
print(first_student.__len__())

#Клас Book з атрибутами title, author, year. Метод get_age (відомості про книжку і буде різницю
#між зараз роком і роком видання


#Клас квадрат (атрибут - сторона) з методом get_perim для обчислення периметра

third_student = Student()
third_student.age = int(input("Введіть Ваш вік"))