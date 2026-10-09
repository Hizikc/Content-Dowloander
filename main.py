import sys
import os


# Функция главного меню
def main():
    while True:
        # Очистка терминала перед выводом меню
        os.system('cls')
        # Меню
        print('YouTube-Dowloander')
        print('1. Загрузка')
        print('2. Настройка')
        print('0. Выход')
        
        choise = input(': ')
        
        if choise == '1':
            d()
        elif choise == '2':
            s()
        elif choise == '0':
            os.system('cls')
            break
        
if __name__ == '__main__':
    main()