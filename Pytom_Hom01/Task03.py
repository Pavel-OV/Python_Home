# ; Задача 6: Вы пользуетесь общественным транспортом? 
# ; Вероятно, вы расплачивались за проезд и получали билет с номером.
# ;  Счастливым билетом называют такой билет с шестизначным номером,
# ;   где сумма первых трех цифр равна сумме последних трех.
# ;    Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# ;    Вам требуется написать программу, которая проверяет счастливость билета.

# ; Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# ;  если разрешается сделать один разлом по прямой между дольками 
# ;  (то есть разломить шоколадку на два прямоугольника).
# ; Задача 2: - HARD необязательная, идет за 3 обязательных.
# ; Найдите сумму цифр любого вещественного или целого числа.
# ;  Можно использовать decimal. Через строку решать нельзя.
print('Проверте счастливый ли билет.')
bilet=int(input('Номер билета\n'))
sum1=0
sum2=0
count=1
while(bilet>9):
    if(count<4):
        didital=bilet%10
        sum1=sum1+didital
        bilet=bilet//10
    else:
            didital=bilet%10
            sum2=sum2+didital
            bilet=bilet//10
       
    count=count+1
else:
    sum2=sum2+bilet
    if(sum1!=sum2 and count>6):
       print('билет может быть и счасливый, но набранное число больше шести знаков ')
    if (count<6):
        print('билет может быть и счасливый, но набранное число меньше шести знаков ')

    if (sum1==sum2 and count==6):
        print('Билет счасливый')
