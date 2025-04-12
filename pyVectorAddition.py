import numpy as np 

class Menu:
        
    def __init__(self, title : str):
        self.title = title
        
    def display_title(self):
        print(f'{self.title}')

class Vector:
    
    def __init__(self, vectorA: float, vectorB: float, angle_a: float, angle_b: float):
        self.vectorA = vectorA
        self.vectorB = vectorB
        self.angle_a = np.deg2rad(angle_a)
        self.angle_b = np.deg2rad(angle_b)
    
    def get_vectorA(self):
        return f'Vector A: {self.vectorA}'
    
    def get_vectorB(self):
        return f'Vector B: {self.vectorB}'
    
    def get_angle_a(self):
        return f'Angle of Vector A: {self.angle_a: .2f}'
    
    def get_angle_b(self):
        return f'Angle of Vector B: {self.angle_b: .2f}'
    
class VectorAdd(Vector):
        
    def __init__(self, vectorA: float, vectorB: float, angle_a: float, angle_b: float):
        super().__init__(vectorA, vectorB, angle_a, angle_b)
        
    def add_vectors(self):
        vector_a_xy = np.array([self.vectorA * np.cos(self.angle_a), self.vectorA * np.sin(self.angle_a)])
        vector_b_xy = np.array([self.vectorB * np.cos(self.angle_b), self.vectorB * np.sin(self.angle_b)])
        vector_sum = vector_a_xy + vector_b_xy
        resultant = round(np.sqrt(vector_sum[0]**2 + vector_sum[1]**2))
        
        return f'Magnitude of resultant vector = {resultant}'
    

title = Menu('Welcome to Python Vector Addition!')
title.display_title()

print(f'\n')

# User Input
vectorA = float(input('Enter the first vector: '))
angle_a = float(input('Enter the angle of the first vector: '))

vectorB = float(input('Enter the second vector: '))
angle_b = float(input('Enter the angle of the second vector: '))

vector_instance = Vector(vectorA, vectorB, angle_a, angle_b)

print_vA = vector_instance.get_vectorA()
print_vB = vector_instance.get_vectorB()
print_angleA = vector_instance.get_angle_a()
print_angleB = vector_instance.get_angle_b()

# Print the vectors and angles
vector_instance = Vector(vectorA, vectorB, angle_a, angle_b)

print(f'\n')

print(f'Components of Vector A: \n{vector_instance.get_vectorA()}\n{vector_instance.get_angle_a()}')
print(f'\nComponents of Vector B: \n{vector_instance.get_vectorB()}\n{vector_instance.get_angle_b()}')

print(f'\n')

# Vector Addition
vector_add = VectorAdd(vectorA, vectorB, angle_a, angle_b)
result = vector_add.add_vectors()
print(result)