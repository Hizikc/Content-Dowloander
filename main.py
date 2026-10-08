import sys
import os

def main():
    while True:
        os.system('cls')
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