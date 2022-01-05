# Пульт охраны банка
Пульт охраны можно подлючить к удалённой базе данных. Сайт выводит список сотрудников банка с активными картами доступа и список тех, кто сейчас находится в хранилище с указанием времени пребывания.

Также сайт позволяет посмотреть историю посещений хранилища для любого выбранного сотрудника. Для каждого посещения выводится дата, время и продолжительность пребывания в хранилище.

Если сотрудник находится в хранилище более часа, система отмечает данный визит как подозрительный.

## Установка и запуск сайта
Скачайте код:
```
https://github.com/nekto007/watching-storage.git
```
Перейдите в каталог проекта:
```
cd watching-storage
```
Установите зависимости в виртуальное окружение:
```
pip install -r requirements.txt
```
Создайте .env файл с конфигурацией
```
DB_SETTINGS=postgres://USER:PASSWORD@HOST:PORT/NAME
```
Запустите сайт:
```
python manage.py runserver 8000
```
Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Дополнительные настройки в .env
```
SECRET_KEY=YOUR_KEY
DEBUG=true
```