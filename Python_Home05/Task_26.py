# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def calculate_degree(numberA,numberB):
    if numberB==1:
        return numberA
    if numberB!=1:
        return numberA*(calculate_degree(numberA,numberB-1))
numberA=int(input('Введите число А='))
numberB=int(input('Введите число В='))
print(f'Результат возведения числа {numberA} в степень {numberB} равен', calculate_degree(numberA,numberB))
 