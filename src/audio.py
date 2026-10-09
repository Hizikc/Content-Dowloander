import os
import main
import config

def audio():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('1. Стандарт')
        print('2. С доп параметрами')
        print('0. Выход')
        
        ao = input(': ')
        
        if ao == '1':
            print(':')
        elif ao == '2':
            print(':')
        elif ao == '0':
            os.system('cls')
            main.main()
            break