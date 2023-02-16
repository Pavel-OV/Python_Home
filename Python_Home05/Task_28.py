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


# s=input('введите выражение')
# operatory=["+",'-','/','*']
# print(operatory)
# s=list(s)
# digital=[]
# for i in s:
#     text=''
#     if i.isdigit():
#         text=''.join([text,i])
#         sp=int(text)
#         digital.append(sp) 
# print(digital,type(digital))
# сделать функцию
# for i in digital:
#     i=str(i)
#     for j in s:
        
#         if i==j: s[j]=digital[i]
#         print(type(s[j]))

# print('sp',sp,type(sp))

#     # for j in operatory:
#     #     if ==int[i]
#     # print(s[i])

# print(s)
# print(s.count(int))

