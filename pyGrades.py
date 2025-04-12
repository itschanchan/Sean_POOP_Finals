from abc import ABC, abstractmethod

class Menu:
    def __init__(self, title: str):
        self.title = title
        
    def display_title(self):
        print(f'{self.title}')

# Abstract class Student
class Student(ABC):

    total_students = 0      
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def __str__(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"

    @abstractmethod
    def get_school_count(self):
        pass

    @abstractmethod
    def get_ave_GPA(self):
        pass

# SchoolOne class inheriting from Student (abstract class)
class SchoolOne(Student):
    
    SchoolOne_count = 0
    total_GPA = 0

    def __init__(self, name, grade):
        super().__init__(name, grade)
        SchoolOne.SchoolOne_count += 1
        SchoolOne.total_GPA += grade

    def get_school_count(self):
        return f'Total no. of students in SchoolOne: {SchoolOne.SchoolOne_count}'

    def get_ave_GPA(self):
        if SchoolOne.SchoolOne_count == 0:
            return f"No students enrolled in SchoolOne"
        else:
            return f'SchoolOne Average: {SchoolOne.total_GPA / SchoolOne.SchoolOne_count:0.2f} GPA'

# SchoolTwo class inheriting from Student (abstract class)
class SchoolTwo(Student):
    
    SchoolTwo_count = 0
    total_GPA = 0

    def __init__(self, name, grade):
        super().__init__(name, grade)
        SchoolTwo.SchoolTwo_count += 1
        SchoolTwo.total_GPA += grade

    def get_school_count(self):
        return f'Total no. of students in SchoolTwo: {SchoolTwo.SchoolTwo_count}'

    def get_ave_GPA(self):
        if SchoolTwo.SchoolTwo_count == 0:
            return f"No students enrolled in SchoolTwo"
        else:
            return f'SchoolTwo Average: {SchoolTwo.total_GPA / SchoolTwo.SchoolTwo_count:0.2f} GPA'

# Welcome Screen
title_screen = Menu('Welcome to Python Student Grade Calculator!')
title_screen.display_title()

print(f'\n')

# School One
school_one_student1 = SchoolOne('John Doe', 85)
school_one_student2 = SchoolOne('Alice Smith', 92)
school_one_student3 = SchoolOne('Bob Johnson', 78)
school_one_student4 = SchoolOne('Charlie Brown', 88)
school_one_student5 = SchoolOne('Daisy Miller', 95)

print(f'{school_one_student1.get_school_count()}')
print(f'{school_one_student1.get_ave_GPA()}')

print(f'\n' + '-'*50 + '\n')

# School Two
school_two_student1 = SchoolTwo('Eve Davis', 90)
school_two_student2 = SchoolTwo('Frank Wilson', 82)
school_two_student3 = SchoolTwo('Grace Lee', 87)
school_two_student4 = SchoolTwo('Henry Taylor', 91)
school_two_student5 = SchoolTwo('Ivy Anderson', 89)

print(f'{school_two_student1.get_school_count()}')
print(f'{school_two_student1.get_ave_GPA()}')
