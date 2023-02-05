#  Задача 12:Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
from random import randint
print('Петя задумывает два натуральных числа X и Y (X,Y≤1000)')
first_number=randint(0,1000)
secont_number=randint(0,1000)
print('Катя должна их отгадать, у неё две подсказки')
sum=first_number+secont_number
print(f'Первая подсказка, сумма чисел={sum}')
multiplicatio=first_number*secont_number
print(f'Вторая подсказка, умножение чисел={multiplicatio}')
# x=int(input('X='))
# y=int(input('Y='))
# sum1=x+y
# multiplicatio1=x*y
#try:
# while(x+y!=sum and y*x!=multiplicatio):
#         print(x,y)
#         print(first_number,secont_number,sum,multiplicatio)
#         x=int(input('X='))
#         y=int(input('Y='))
# print('hhhhh')
for i in range(sum):
    for w in range(multiplicatio):
        if (i+w==sum and i*w==multiplicatio): print('числа равны',i,w)
    


        

    
    
             
   
        
            



