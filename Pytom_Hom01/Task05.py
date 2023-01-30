# ; Задача 2: - HARD необязательная, идет за 3 обязательных.
# ; Найдите сумму цифр любого вещественного или целого числа.
# ;  Можно использовать decimal. Через строку решать нельзя.
from decimal import Decimal
number=Decimal(input('Введите вещественное или целогое число ='))
while number != int(number):
    number=number* 10
number=int(number)
print(f'Теперь подсчитаем сумму цифр этого числа',number)
digit=0
while number>9:
    count=number%10
    digit=digit+count
    number=number//10
else:
    digitl=digit+number
print(digitl)


#didital=Decimal(Decimal(d).as_tuple().exponent*(-1))
# print(didital)
# print (Decimal(str(0.25456466424685)).as_tuple().exponent*(-1))



# foo = a % 10
# if foo != 0:
#     # Then foo contains decimals
#     pass

# if foo == 0:
#     # Then foo does NOT contain decimals Тогда foo не содержит десятичных знаков
#     print('ghjgjjj')

#     y=True if y>50 else False
