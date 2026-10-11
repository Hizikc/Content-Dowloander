import os
import main
import config
import src.video_standard as video_standard
import src.custom_video as custom_video

def video():
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
            video_standard.video_standard()
        elif ao == '2':
            custom_video.custom_video()
        elif ao == '0':
            os.system('cls')
            main.main()
            break