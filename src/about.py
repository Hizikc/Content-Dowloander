import os
import config

def about():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print()
        print('Developer: hizikc')
        print('-----------------')
        print('version: In development')
        print()
        print('0. Выход')
        
        about = input(': ')
        
        if about == '0':
            return