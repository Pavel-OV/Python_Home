from function_spr import*


# "C:\Users\Степан\Pictures\phones.json"
# "D:\Python_Home\Python_Home08_phones\phones.json"
print_help()
try:
    command = int(input('Выберите команду'))
    while command !=0:
        if command ==1:
            list_sprav()
        elif command ==2:
            save()
        elif command ==3:
            search=input("Введите данные: ")
            data_seafch(search)
        elif command ==4:
            print_help()
        elif command ==0:
            break
        else:
            print("Такой команды нет в списке!")
        command =int(input('Выберите команду:'))
except ValueError:
    print("Введены не корректные данные!")

# with open("phones.json","r",encoding="utf-8") as fh:
#         fh=json.load(fh)
# while True:
#     command=input("Введите команду ")
#     if command == "start": 
#         print("Бот - фильмотека начал свою работу")
#         load()
#     elif command=="7":
#         save()
#         print('Бот остановил свою работу. Заходите ещё раз. будем рады!')
#         break
#     elif command=="2":
#         print('Вот текущий список фильмов')
#         print(telephone_directory)
#     elif command == "/add":
#         f=input('Введите название фильма ')
#         telephone_directory.append(f)
#         print('Фильм был успешно добавлен в коллекцию!')
#     elif command =="/help" :
#         print('Инструкция находится здесь')
#     elif command=="/delete":
#         f=input('Введите название фильма, который надо удалить')
#         '''
#         if f in films:
#             films.remove(f)
#             print('Фильм был успешно удалён!')
#         else:
#             print('Такого фильма в фильмотеке нет')
#            '''
#         try:
#              telephone_directory.remove(f)
#              print('Фильм был успешно удалён!')
#         except:
#              print('Такого фильма в фильмотеке нет')
#     elif command=="/random":
#         #rnd=randint(0,len(films)-1)
#         #print("Слепой жребий выпал вам на фильм - "+ films[rnd])
#         print("Слепой жребий выпал вам на фильм - "+ choice(telephone_directory))
#     elif command =="/save":
#         save()
#     elif command=="/load":
#         load()
#         print("Фильмотека успешно загружена")     


#     else:
#         print('Неопознанная команда. Просьба изучить инструкцию через / help')    