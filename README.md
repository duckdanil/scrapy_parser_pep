### Проект: асинхронный парсер PEP.
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTujwu6HtzvrpKw44xso5zi1iYZvFeDtWzr4_FO5En6DQ&s)
#### Содержание
1. Описание проекта
2. Установка
3. Запуск
***
### 1. *Описание проекта*


Parameter  | Value
-------------|:-------------
Наименование проекта  | scrapy_parser_pep
Назначение проекта | создать парсер документов PEP на базе фреймворка Scrapy (PEP - Python Enhancement Proposals)
Tech Stack. Client. OS | Windows, Linux, MacOS
GitHub | https://github.com/duck.danil/scrapy_parser_pep
Author | Danil Utkin , duck.danil@yandex.ru

### 2. *Установка*




2.1. клонировать репозиторий
```
cd dev
git clone  https://github.com/duck.danil/scrapy_parser_pep
```
2.2. создать и активировать виртуальное окружение:
```
  # Windows
python -m venv env
. env/Scripts/activate
  # Unix / MacOS
python3 -m venv env
source venv/bin/activate
```
2.3. обновить менеджер пакетов pip, установить зависимости requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. *Запуск*


```
 ввести команду: запустить паука
```
scrapy crawl pep
```
3.4. вывод результата <запуска паука>:
* файл_1:

Parameter  | Value
-------------|:-------------
Директория  | /results
Наименование файла   | pep_ДатаВремя.csv, пример: pep_2023-05-11T18-04-02.csv
Формат файла   | csv
Состав полей   | number,name,status 
Описание полей  | 1)number - номер PEP; 2) name - наименование PEP; 3)status - статус PEP;
Структура файла  | Первая запись - шапка; Каждая запись - один документ PEP;

* файл_2:

Parameter  | Value
-------------|:-------------
Директория  | /results
Наименование файла   | status_summary_ДатаВремя.csv, пример: status_summary_2023-05-11_21-04-31.csv
Формат файла   | csv
Состав полей   | Статус, Количество
Описание полей  | 1)Статус - уникальный статус документов PEP; 2) Количество - количество документов PEP, которые имеют данный статус;
Структура файла  | Первая запись - шапка; Последняя запись - ИТОГО количество документов PEP; Каждая запись - уникальный статус документов PEP;