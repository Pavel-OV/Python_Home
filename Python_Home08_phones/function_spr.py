import json
def print_help():
    print(""""
0 - Выход
1 - Показать справочник
2 - Сохранить справочник
3 - Поиск абонента
4 - Помощь """)

def list_sprav():
    with open("phones1.json",'r',encoding="utf-8") as fl:
        print(fl.read())

def save():
    with open("phones.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(telephone_directory,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")
def load():
     with open("phones.json","r",encoding="utf-8") as fh:
        telephone_directory=json.load(fh)
     print("Фильмотека успешно загружена")   