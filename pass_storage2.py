#Импорт библиотек
import time
import os
from getpass import getpass as gp
import pyAesCrypt


#Словарь для хранения данных внутри программы
#os.system("cls||clear") - очистка консоли от предыдущих записей


pass_set={}

#Функция для шифрования файлов
def encription(file, password):
    buffer_size= 512*1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+".crp",
        password,
        buffer_size
     )

    os.remove(file)

#Функция для дешифровки файлов
def decryption(file, password):
    buffer_size= 512*1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
     )

    os.remove(file)

#Функция приветствия и ее вызов
def hello():
    print("Добро пожаловать!")
    time.sleep(1)
    os.system("cls||clear")

hello()


#Функция работы с хранилищем
def storage():
    os.system("cls||clear")
    print("Что вы хотите сделать?\n"+"#"*15+"\n1. Посмотреть пароли\n2. Добавить пароль\n3. Выйти")
    stor=int(input())

    if stor==1:
        os.system("cls||clear")
        pass_set={}
        
        if os.path.exists('out.txt.crp'):
            password=(input("Пароль для дешифровки:\n"))
            decryption('out.txt.crp', password)
        else:
            os.system("cls||clear")

        with open('out.txt') as inp:
            for i in inp.readlines():
                key,val = i.strip().split(':')
                pass_set[key] = val
        for key, value in pass_set.items():
            print(f'{key} : {value}')
        
        print("#"*20)

        print("1.Выход")
        inp=input()
        if inp=="1":
            storage()

    elif stor==2:
        add_info()
        print("Это все?")
        da=int(input("1. Да\n2. Нет\n"))

        if da==1:
            print("Зашифровать файл?")
            net=int(input("1. Да\n2. Нет\n"))

            if net==1:
                password=input("Пароль: ")
                encription('out.txt', password)
                storage()

        elif da==2:
            add_info()

        else:
            choose_move

    elif stor==3:
        choose_move()
    else:
        storage()
  
#Функция проверки данных при регистрации
def check(log, password):
    if log=="Ваш логин" and password=="ваш пароль":   
        storage()    
    else:
        print("До свидания")
        time.sleep(2)
        os.system("cls||clear") 

#Функция авторищации, если выбрано хранилище 
def authorization():
    os.system("cls||clear")

    print("Укажите логин и пароль\n"+"#"*22)

    login=input("Логин:\n")
    password=gp("Пароль:\n")

    check(login, password)

#Функция выбора хранилища, либо генерации
def choose_move():
    print("Выберите действие\n"+ "#"*20,"\n1. Хранилище паролей\n2. Генератор паролей\n3. Выход" )

    choose=int(input())

    if choose==3:
        os.system("cls||clear")
    elif choose==1:
        authorization()
        
choose_move()

  
#Функция работы с добавлением информации в хранилище
def add_info():
    log=input("Укажите название ресурса: ")
       
    value=input("Укажите логин и пароль через пробел: ")
    pass_set[log]=value
    if os.path.exists('out.txt.crp'):
        password=input("Пароль для дешифровки:\n")
        decryption('ouy.txt.crp', password)
        
    with open('out.txt','a') as out:
        for key,val in pass_set.items():
            out.write('{}:{}\n'.format(key,val))


