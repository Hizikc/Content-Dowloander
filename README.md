# Content-Dowloander

## CLI-Script для загрузки контента
![images](assets/logo.ico)






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