import os
import main
import config
import src.audio_standard as audio_standard
import src.custom_audio as custom_audio

def audio():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('Аудио')
        print()
        print('1. Стандарт')
        print('2. С доп параметрами')
        print('0. Выход')
        
        ao = input(': ')
        
        if ao == '1':
            audio_standard.audio_standard()
        elif ao == '2':
            custom_audio.custom_audio()
        elif ao == '0':
            os.system('cls')
            main.main()
            break