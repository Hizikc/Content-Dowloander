import os
import yt_dlp
from yt_dlp import YoutubeDL
import config

my_folder_name = 'Content-Dowloand'
music_path = os.path.join(os.environ['USERPROFILE'], 'Music')
target_path = os.path.join(music_path, my_folder_name)

if not os.path.exists(target_path):
    os.makedirs(target_path)

def show_finished_name(d):
    if d['status'] == 'finished':
        filename = os.path.basename(d['filename'])
        print(f'\n[УСПЕШНО СКАЧАНО]: {filename}')
        input('\nНажми Enter, чтобы продолжить...')

options_music = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(target_path, '%(uploader)s - %(title)s.%(ext)s'), 
    'noplaylist': False,
    'ignoreerrors': True,
    'writethumbnails': True,
    'already_have_thumbnail': False,
    'nooverwrites': True,
    'forceoverwrites': False,
    'progress_hooks': [show_finished_name],
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        },
        {
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        },
        {
            'key': 'EmbedThumbnail',
            'already_have_thumbnail': False,
        }
    ],
}

def audio_standart():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        print('Введите 0 для выхода')
        url = input('Введите ссылку для скачивания: ')
        
        if url == '':
            continue
            
        if url == '0':
            break

        with YoutubeDL(options_music) as ydl:
            ydl.download([url])
