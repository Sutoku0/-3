import math

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))

print(f"Площадь прямоугольника: {calculate_rectangle_area(width, height):.2f}")
radius = float(input("Введите радиус круга: "))
print(f"Площадь круга: {calculate_circle_area(radius):.2f}")