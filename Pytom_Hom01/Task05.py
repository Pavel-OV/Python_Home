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
count_digit=0
while number>9:
    count=number%10
    digit=digit+count
    number=number//10
    count_digit=count_digit+1
else:
    digitl=digit+number
    count_digit=count_digit+1
print(f"Сумма цифр ={digitl} \n колличество цифр ={count_digit}")
