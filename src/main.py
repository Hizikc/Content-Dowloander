import sys
import os
import menu_downloander as menu_downloander
import about
import config

# Функция главного меню
def main():
    while True:
        # Очистка терминала перед выводом меню
        os.system('cls')
        # Меню
        print(config.APP_NAME)
        print()
        print('1. Загрузка')
        print('2. О программе')
        print('0. Выход')
        
        choise = input(': ')
        
        if choise == '1':
            menu_downloander.menu_downloander()
        elif choise == '2':
            about.about()
        elif choise == '0':
            os.system('cls')
            sys.exit()
            break
        
if __name__ == '__main__':
    main()