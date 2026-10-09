import os
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
        
        dr = input(': ')
        
        if dr == '1':
            video.video()
        elif dr == '2':
            audio.audio()
        elif dr == '0':
            os.system('cls')
            main.main()
            break
