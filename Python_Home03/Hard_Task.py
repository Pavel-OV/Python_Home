# Обязательные задачи в презентации.

# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
spisok=[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]
print(spisok)
min=max=midl=0
min=spisok[0]
max=spisok[1]
if max<min:
     max=spisok[0]
     min=spisok[1]
for i in range (len(spisok)):
     if min>spisok[i]: min=spisok[i]
     if max<spisok[i]: max=spisok[i]
print(f"Итервал от{min} до {max}")
count=0
intervalmin=min
intervalmax=max
for min in range(len(spisok)):
     for i in range(len(spisok)):
          #print(f'Итерация{min}')
          if min==spisok[i]:
               print(i,spisok[i],min)
               count=count+1
               intervalmin=spisok[i]
               print(count)
               break
          else:
               continue
     
          # else:
          #      print(f'В интервале отсуствует {min}')

# for(min) in range(len(spisok)):
#      if min==spisok[i]:
#                print(i,spisok[i],min)
#                count=count+1
#                intervalmin=spisok[i]
#                print(count)
            



       

     
   


    

