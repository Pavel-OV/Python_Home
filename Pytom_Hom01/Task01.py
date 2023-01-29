# ; Задача 2: Найдите сумму цифр трехзначного числа.

print ('Найти сумму цифр трехзначного числа')
number=int(input('Введите число ='))
summer_number=0
count=0
while (number>9):
    didit=number%10 
    number=number//10
    summer_number=summer_number+didit
    count=count+1
else:
    summer_number=summer_number+number
    count=count+1
print('Количество цифр введённого числа=', count)
print('Сумма цифр введённого числа=', summer_number)   




