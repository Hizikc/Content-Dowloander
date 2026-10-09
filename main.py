import sys
import os
import dowloander
import settings

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
            dowloander.dowloander()
        elif choise == '2':
            settings.settings()
        elif choise == '0':
            os.system('cls')
            break
        
if __name__ == '__main__':
    main()