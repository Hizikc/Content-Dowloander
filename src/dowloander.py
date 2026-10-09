import os
import sys
import main
import config
import video
import audio

# Функция меню загрузки
def dowloander():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('1. Видео')
        print('2. Аудио')
        print('0. Выход')
        
        dm = input(': ')
        
        if dm == '1':
            video.video()
        elif dm == '2':
            audio.audio()
        elif dm == '0':
            os.system('cls')
            main.main()
            break
