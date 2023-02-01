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
print(first_number),print(secont_number)
# if (x>50):
#     y=True
# else:
#     y=False
# print(f"сгенерированное число х",{x})
# print(y)


