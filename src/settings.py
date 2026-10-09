import sys
import os 
import main
import config

def settings():
    while True:
        print(config.APP_NAME)
        print('0. Выход')
        
        ss = input(': ')
        
        if ss == '0':
            os.system('cls')
            main.main()
        break