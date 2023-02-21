from  random import *
import json
films=[]
def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")
def load():
     with open("films.json","r",encoding="utf-8") as fh:
        fh=json.load(fh)
     print("Фильмотека успешно загружена")  
try:
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека успешно загружена") 
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властилин колец")
    films.append("Чебурашка") 
    films.append("Ликвидация") 

# films.append("Матрица")
# films.append("Солярис")
# films.append("Властилин колец")
# films.append("Чебурашка") 
# films.append("Ликвидация")

while True:
    command=input("Введите команду ")
    if command == "start": 
        print("Бот - фильмотека начал свою работу")
    elif command=="2":
        save()
        print('Бот остановил свою работу. Заходите ещё раз. будем рады!')
        break
    elif command=="2":
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
    elif command =="/save":
        save()
    elif command=="/load":
        with open("films.json","r",encoding="utf-8") as fh:
             fh=json.load(fh)
        print("Фильмотека успешно загружена")     


    else:
        print('Неопознанная команда. Просьба изучить инструкцию через / help')    
