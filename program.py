# program.py
from datetime import date


sum = 1 + 2
print (sum)

left_side = 10
right_side = 5
print(left_side / right_side)

date.today()
print(date.today())

print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduce tu nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))