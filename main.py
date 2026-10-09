import sys
import os

# Переменная имени приложения
APP_NAME = 'YouTube-Dowloander'

# Функция меню загрузки
def dowloander():
    while True:
        os.system('cls')
        print(APP_NAME)
        print('1. Видео')
        print('2. Аудио')
        print('0. Выход')
        
        dm = input(': ')
        
        if dm == '1':
            dowloander.video()
        elif dm == '2':
            dowloander.audio()
        elif dm == '0':
            os.system('cls')
            main()
            break

# Функция главного меню
def main():
    while True:
        # Очистка терминала перед выводом меню
        os.system('cls')
        # Меню
        print(APP_NAME)
        print('1. Загрузка')
        print('2. Настройка')
        print('0. Выход')
        
        choise = input(': ')
        
        if choise == '1':
            dowloander()
        elif choise == '2':
            s()
        elif choise == '0':
            os.system('cls')
            break
        
if __name__ == '__main__':
    main()