import os 
import main
import config

def about():
    while True:
        print(config.APP_NAME)
        print('Developer: hizikc')
        print('version: 1.0.0')
        print('0. Выход')
        
        ss = input(': ')
        
        if ss == '0':
            os.system('cls')
            main.main()
        break