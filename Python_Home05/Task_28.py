# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum_numbers(numberA,numberB):
    if numberB==0:
        return numberA
    else:
        if numberB>0 : 
            return sum_numbers(numberA+1,numberB-1)
        else: 
            numberB<0 
            return sum_numbers(numberA-1,numberB+1)
 
numberA=int(input('Введите число А='))
numberB=int(input('Введите число В='))
print(sum_numbers(numberA,numberB))


