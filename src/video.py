import os
import main
import config
import video_standart
import video_not_standart

def audio():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('1. Стандарт')
        print('2. С доп параметрами')
        print('0. Выход')
        
        ao = input(': ')
        
        if ao == '1':
            video_standart.video_standart()
        elif ao == '2':
            video_not_standart.video_not_standart()
        elif ao == '0':
            os.system('cls')
            main.main()
            break