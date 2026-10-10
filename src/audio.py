import os
import main
import config
import audio_standart
import audio_not_standart

def audio():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('Видео')
        print('')
        print('1. Стандарт')
        print('2. С доп параметрами')
        print('0. Выход')
        
        ao = input(': ')
        
        if ao == '1':
            audio_standart.audio_standart()
        elif ao == '2':
            audio_not_standart.audio_not_standart()
        elif ao == '0':
            os.system('cls')
            main.main()
            break