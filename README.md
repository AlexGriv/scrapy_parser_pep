# Проект парсинга документации PEP с помощью Scrapy parser
Парсинг информации:
https://peps.python.org/

## Описание
-Сбор информации о статусах версий Python.
-Собранная информация записывается в файлы

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке
Cоздать и активировать виртуальное окружение
Обновить PIP
Установить зависимости из файла requirements.txt
Запустить парсинг через scrapy

git clone https://github.com/AlexGriv/scrapy_parser_pep.git
python3 -m venv env
source env/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
scrapy crawl pep

Например:


## Встроенные парсеры
*pep*

## Автор
Гривцов А.С.