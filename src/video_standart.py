import os
import yt_dlp
from yt_dlp import YoutubeDL
import config

video_path = os.path.join(os.environ['USERPROFILE'], 'Videos')
target_path = os.path.join(video_path, 'My_Videos')

if not os.path.exists(target_path):
    os.makedirs(target_path)

def show_finished_name(d):
    if d['status'] == 'finished':
        filename = os.path.basename(d['filename'])
        print(f'\n[УСПЕШНО СКАЧАНО]: {filename}')
        input('\nНажми Enter, чтобы продолжить...')

options_video_std = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': os.path.join(target_path, '%(title)s.%(ext)s'), 
    'noplaylist': False,
    'ignoreerrors': True,
    'nooverwrites': True,
    'forceoverwrites': False,
    'progress_hooks': [show_finished_name],
}

def video_standart():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        
        url = input('Введите ссылку для скачивания видео (Стандарт): ')
        
        if url == '':
            continue
            
        if url == '0':
            break

        with YoutubeDL(options_video_std) as ydl:
            ydl.download([url])
