# Content-Dowloander

## CLI-Script для загрузки контента
![images](assets/logo.ico)

## Установка:
### Для установки систему скачайте и запустите файл `Content_Downloader_Installer_v1.0.0.exe` 
### Для установки протативной версии программы скачайте и запустите файл `Content_Downloader_Portable_v1.0.0.exe`




## Комипиляция:

### Для самостоятельной компиляции необходимо установить библеотеки из файла `requirements.txt` командой:
```bash
pip install -r requirements.txt
```
### После чего выполнить команду:
```bash
pyinstaller --onefile --paths="src" --distpath="docs" --icon="assets/logo.ico" --name="Content-Downloader" src/main.py
```
### После завершения команды exe файл появится в папке docs 

## Создание установщика
### Для того чтобы создать файл установки необходимо установить программу `