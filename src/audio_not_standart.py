import os
import yt_dlp
from yt_dlp import YoutubeDL
import config

music_path = os.path.join(os.environ['USERPROFILE'], 'Music')

def show_finished_name(d):
    if d['status'] == 'finished':
        filename = os.path.basename(d['filename'])
        print(f'\n[УСПЕШНО СКАЧАНО]: {filename}')
        input('\nНажми Enter, чтобы продолжить...')

def audio_not_standart():
    while True:
        os.system('cls')
        print(config.APP_NAME)
        
        url = input('Введите ссылку для скачивания: ')
        
        if url == '':
            continue
            
        if url == '0':
            break

        print('\nВыбери битрейт звука (1 - 320kbps, 2 - 256kbps, 3 - 192kbps): ')
        bitrate_choice = input('Цифра: ')
        
        if bitrate_choice == '2':
            quality = '256'
        elif bitrate_choice == '3':
            quality = '192'
        else:
            quality = '320'

        user_folder = input('\nВведите название папки внутри "Музыки" (Enter для дефолта): ')
        if user_folder == '':
            user_folder = 'My_Music_Custom'
            
        target_path = os.path.join(music_path, user_folder)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        options_non_music = {
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
                    'preferredquality': quality,
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

        with YoutubeDL(options_non_music) as ydl:
            ydl.download([url])
