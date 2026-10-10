# Content-Dowloander

## CLI-Script для загрузки контента
![images](assets/logo.ico)

## Установка:
### Для установки в систему скачайте и запустите файл:
#### `Content_Downloader_Installer_v1.0.0.exe` 
### Для установки протативной версии программы скачайте и запустите файл:
#### `Content_Downloader_Portable_v1.0.0.exe`




## Комипиляция:

### Для самостоятельной компиляции необходимо установить библеотеки из файла:
### `requirements.txt` 
### командой:
```powershell
pip install -r requirements.txt
```
### После чего выполнить команду:
```powershell
pyinstaller --onefile --paths="src" --distpath="docs" --icon="assets/logo.ico" --name="Content-Downloader" src/main.py
```
### После завершения команды exe файл появится в папке docs 

## Создание установщика:
### Для того чтобы создать файл установки необходимо установить программу 
### [`Inno Setup 7`](https://jrsoftware.org/isinfo.php)
### В ней открыть файл [`installer_config.iss`](installer_config.iss)

### и запустить сборку кнопкой в интерфейсе:
![](assets/Inno%20Setup%207.png)
### или горячими клавишами:
### `ctrl+F9`