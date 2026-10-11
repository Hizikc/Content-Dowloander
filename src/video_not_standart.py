import os
import yt_dlp
from yt_dlp import YoutubeDL
import config

video_path = os.path.join(os.environ['USERPROFILE'], 'Videos')

def show_finished_name(d):
    if d['status'] == 'finished':
        filename = os.path.basename(d['filename'])
        print(f'\n[УСПЕШНО СКАЧАНО]: {filename}')
        input('\nEnter, чтобы продолжить...')

def video_non_standart():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        
        url = input('Введите ссылку для скачивания видео (Нестандарт): ')
        
        if url == '':
            continue
            
        if url == '0':
            break

        print('\nМаксимальное качество видео:')
        print('1 - 1080p (FullHD)')
        print('2 - 720p (HD)')
        print('3 - 480p')
        print('4 - Максимально возможное (4K и выше)')
        res_choice = input(': ')
        
        if res_choice == '1':
            fmt = 'bestvideo[height<=1080]+bestaudio/best'
        elif res_choice == '2':
            fmt = 'bestvideo[height<=720]+bestaudio/best'
        elif res_choice == '3':
            fmt = 'bestvideo[height<=480]+bestaudio/best'
        else:
            fmt = 'bestvideo+bestaudio/best'

        user_folder = input('\nНазвание папки внутри "Видео" (Enter для дефолта): ')
        if user_folder == '':
            user_folder = 'Content_Dowloander'
            
        target_path = os.path.join(video_path, user_folder)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        options_video_non = {
            'format': fmt,
            'outtmpl': os.path.join(target_path, '%(title)s.%(ext)s'), 
            'noplaylist': False,
            'ignoreerrors': True,
            'nooverwrites': True,
            'forceoverwrites': False,
            'progress_hooks': [show_finished_name],
        }

        with YoutubeDL(options_video_non) as ydl:
            ydl.download([url])
