# Учебный парсер ScrapyPEP
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

```ScrapyPEP-парсер``` - парсер документов PEP на базе фреймворка Scrapy
## Технологии:
- Python 3.11
- Scrapy 2.5.1

## Описание
Парсер собирает информацию с сайтов документации Python и документов PEP.<br>
Информация выводится в виде двух файлов .csv:
- первый файл содержит список всех PEP: номер, название и статус.
- второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе.

### Запуск парсера
```
$ scrapy crawl pep
```
После запуска парсера будет создана папка results с двумя csv-файлами.


### Как развернуть проект на компьютере:
1. Клонировать репозиторий c GitHub на компьютер
```
$ git clone https://github.com/DashaMalva/scrapy_parser_pep.git
```
2. Создать и активировать виртуальное окружение
```
$ python -m venv venv
$ source venv/Scripts/activate
```
3. Обновить менеджер пакетов pip
```
$ python -m pip install --upgrade pip
```
4. Установить зависимости из requirements.txt
```
$ pip install -r requirements.txt
```

### Лицензия
The MIT License (MIT)

### Автор проекта
Студент Яндекс.Практикум,<br>
Дарья Матвиевская
