#Реализуйте функцию внутри класса для расчета углов между сторонами треугольника
import math

class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError ("Простите, но данный треугольник не может сущетсвовать")

        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    @property
    def square(self):
        p = self.perimeter / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

    def angles(self):
        angle_a = math.degrees(
            math.acos(
                (self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__b * self.__c)))
        angle_b = math.degrees(
            math.acos(
                (self.__a ** 2 + self.__c ** 2 - self.__b ** 2) / (2 * self.__a * self.__c)))
        angle_c = math.degrees(
            math.acos(
                (self.__b ** 2 + self.__a ** 2 - self.__c ** 2) / (2 * self.__b * self.__a)))
        return angle_a, angle_b, angle_c
    
try:
    triangle = Triangle(3, 5, 7)

    print("периметр:", triangle.perimeter)
    print("площадь:", triangle.square)
    print("углы:", triangle.angles())

except ValueError as error:
    print("ошибка:", error)
