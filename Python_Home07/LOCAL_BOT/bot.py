from  random import *
import jose
films=[]
films.append("Матрица")
films.append("Солярис")
films.append("Властилин колец")
films.append("Чебурашка") 
films.append("Ликвидация")
while True:
    command=input("Введите команду ")
    if command == "start": 
        print("Бот - фильмотека начал свою работу")
    elif command=="/stop":
        print('Бот остановил свою работу. Заходите ещё раз. будем рады!')
        break
    elif command=="/all":
        print('Вот текущий список фильмов')
        print(films)
    elif command == "/add":
        f=input('Введите название фильма ')
        films.append(f)
        print('Фильм был успешно добавлен в коллекцию!')
    elif command =="/help" :
        print('Инструкция находится здесь')
    elif command=="/delete":
        f=input('Введите название фильма, который надо удалить')
        '''
        if f in films:
            films.remove(f)
            print('Фильм был успешно удалён!')
        else:
            print('Такого фильма в фильмотеке нет')
           '''
        try:
             films.remove(f)
             print('Фильм был успешно удалён!')
        except:
             print('Такого фильма в фильмотеке нет')
    elif command=="/random":
        #rnd=randint(0,len(films)-1)
        #print("Слепой жребий выпал вам на фильм - "+ films[rnd])
        print("Слепой жребий выпал вам на фильм - "+ choice(films))
    

    else:
        print('Неопознанная команда. Просьба изучить инструкцию через / help')    
