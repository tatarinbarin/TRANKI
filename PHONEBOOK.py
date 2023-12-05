import json

phonebook = {}

def commands(): # КОМАНДЫ
    print('-' * 104)
    print(' ' * 40, '<- ТЕЛЕФОННЫЙ СПРАВОЧНИК ->')
    print()
    list = ['1 -> Контакты', '2 -> Добавить контакт', '3 -> Сохранение контакта',
     '4 -> Поиск', '5 -> Изменения данных', 
     '6 -> Добавление данных', '7 -> Удаление данных', 
     '8 -> Удаление контакта', '0 -> Закрывает справочник']
    for i in list:
        print(' ' * 40, i)
    print('-' * 104)
    print()

def read(): # Контакты
    with open('data.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        for i,j in a.items():
            print(i,j)
  
def create(): # Добавить контакт
    name = input('Введите имя: ')
    phone = input('Введите номер(а) абонента через запятую: ').split(',')
    email = input('Введите email: ')
    phonebook[name] = {'number' : phone, 'mail' : email}
    
def save(): # Cохранить контакт
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(phonebook, f)
    print('Данные успешно сохранены!')

def search(): # Поиск по имени
    with open('data.json', 'r',encoding='utf-8') as f:
        a = json.load(f)
        num = 1
        name = input('Введите имя контакта: ')
        for i in a:
            if name == i:
                num = 0
                print(a[name])
                print('Контакт успешно найден!')
        if num: print('Такого контакта нет!')

def changes(): # Изменения данных
    with open('data.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        name = input('Введите имя контакта -> ')
        for i in a:
            if name == i:
                print('Контакт найден!')
                print(phonebook[name])
                what = input('Что хотите изменить? -> ')
                if what in phonebook[name]: 
                    phonebook[name][what] = input('Введите изменения: ')
                    print(f'Контакт <{name}> успешно изменён!')
                else: print('Таких данных нет!')
            else: print('Такого контакта нет!')
    with open('data.json', 'w') as f:
        json.dump(phonebook, f)

def add(): # Добавление данных
    with open('data.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        num = 1
        name = input('Введите имя контакта -> ')
        for i in a:
            if name == i:
                num = 0
                print('Контакт найден!')
                print(phonebook[name])
                what = input('Что хотите добавить? -> ')
                phonebook[name][what] = input('Введите данные: ')
                print(f'Контакт <{name}> успешно изменён!')
        if num: print('Такого контакта нет!')
    with open('data.json', 'w') as f:
        json.dump(phonebook, f)

def del_info(): # Удаление данных
    with open('data.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        num = 1
        name = input('Введите имя контакта -> ')
        for i in a:
            if name == i:
                num = 0
                print('Контакт найден!')
                print(phonebook[name])
                what = input('Что хотите удалить? -> ')
                if what in phonebook[name]:
                    del phonebook[name][what]
                    print(f'Контакт <{name}> успешно изменён!')
                else: print('Таких данных нет!')
        if num: print('Такого контакта нет!')
    with open('data.json', 'w') as f:
        json.dump(phonebook, f)

def delete(): # Удаление контакта
    with open('data.json', 'r', encoding='utf-8') as f:
        a = json.load(f)
        name = input('Введите имя контакта -> ')
        for i in a:
            if name == i:
                print('Контакт найден!')
                print(phonebook[name]) 
                del phonebook[name]
                print('Контакт успешно удалён!')
            else: print('Такого контакта нет!')   
    with open('data.json', 'w') as f:
        json.dump(phonebook, f)
    
while True: # Ввод команды
    commands()
    command = input('Команда: > ')
    if command == '1': read()
    elif command == '2': create()
    elif command == '3' : save()
    elif command == '4' : search()
    elif command == '5' : changes()
    elif command == '6' : add()
    elif command == '7' : del_info()
    elif command == '8' : delete()
    elif command == '0' : 
        print('Работа завершена!')
        break
    else: print('Ошибка команды!')


