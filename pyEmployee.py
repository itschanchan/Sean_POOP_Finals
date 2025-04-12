from abc import ABC, abstractmethod

class TitleScreen():
    def __init__(self, title: str):
        self.__title = title

    def display_title(self):
        print(f'{self.__title}')

class Employee(ABC):
    
    exec_count = 0
    senior_count = 0
    junior_count = 0
    
    @abstractmethod
    def __init__(self, name: str, id: int, department: str, position: str):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__position = position
        self.__salary = 0.0
    
    def __str__(self):
        return f"\nEmployee Name: {self.__name}, ID: {self.__id}, Department: {self.__department}, Position: {self.__position}, Salary: {self.__salary}"

    # Getter methods for subclasses
    def _set_salary(self, salary):
        self.__salary = salary

    def _get_name(self):
        return self.__name

    def _get_id(self):
        return self.__id

    def _get_department(self):
        return self.__department

    def _get_position(self):
        return self.__position

    def _get_salary(self):
        return self.__salary
    
    # Employee Counters
    @classmethod
    def get_exec_count(cls):
        return f"Total no. of executives: {cls.exec_count}"
    
    @classmethod
    def get_senior_count(cls):
        return f"Total no. of senior level employees: {cls.senior_count}"
    
    @classmethod
    def get_junior_count(cls):
        return f"Total no. of junior level employees: {cls.junior_count}"
    
    @staticmethod
    def is_valid_employee(position: str):
        return position.title() in ['CEO', 'COO', 'Senior', 'Junior']

class Executives(Employee):
    
    def __init__(self, name: str, id: int, department: str, position: str, salary: float):
        super().__init__(name, id, department, position)
        self._set_salary(salary)
        Employee.exec_count += 1
        
class SeniorLevel(Employee):
    
    def __init__(self, name: str, id: int, department: str, position: str, salary: float):
        super().__init__(name, id, department, position)
        self._set_salary(salary)
        Employee.senior_count += 1

class JuniorLevel(Employee):
        
    def __init__(self, name: str, id: int, department: str, position: str, salary: float):
        super().__init__(name, id, department, position)
        self._set_salary(salary)
        Employee.junior_count += 1

# Title Screen
title_screen = TitleScreen('PyCam Entertainment Productions: Organization Tree\n')
title_screen.display_title()

# Executives
exec1 = Executives('Sean Lacson', 101, 'Management', 'CEO', 150000.00)
exec2 = Executives('Alexa Soria', 102, 'Management', 'COO', 140000.00)

# Senior Level
senior1 = SeniorLevel('John Doe', 103, 'Management', 'Senior Manager', 120000.00)
senior2 = SeniorLevel('Mary Jane', 104, 'Management', 'Senior Manager', 110000.00)
senior3 = SeniorLevel('Peter Parker', 105, 'Management', 'Senior Manager', 115000.00)

# Junior Level
junior1 = JuniorLevel('Jane Doe', 106, 'Management', 'Junior Manager', 80000.00)
junior2 = JuniorLevel('Clark Kent', 107, 'Management', 'Junior Manager', 75000.00)
junior3 = JuniorLevel('Bruce Wayne', 108, 'Management', 'Junior Manager', 70000.00)

# Outputs:
print(f'Executives:')
print(f'{exec1}')
print(f'{exec2}') 
print(f'\n{Employee.get_exec_count()}')

print(f'\nSenior Level:')
print(f'{senior1}')
print(f'{senior2}')
print(f'{senior3}')
print(f'\n{Employee.get_senior_count()}')

print(f'\nJunior Level:')
print(f'{junior1}')
print(f'{junior2}')
print(f'{junior3}')
print(f'\n{Employee.get_junior_count()}')
