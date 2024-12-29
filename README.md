# Парсер PEP 

Парсер документов на базе фреймворка Scrapy. Реализовал вывод собранной информации в два файла .csv:
- Список всех документов;
- Сводка по каждому статусу документа (статус, количество) и общее количество документов.

Для парсинга применял CSS-селекторы.

## Автор 
- Кобелев Андрей Андреевич  
    - [email](mailto:andrey.pydev@gmail.com)
  
## Технологии  
- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [Scrapy](https://docs.scrapy.org/en/latest/)

## Как запустить проект: 
  
Клонировать репозиторий и перейти в него в командной строке:  
  
```  
git clone https://github.com/andrey-kobelev/scrapy_parser_pep.git
```  
  
```  
cd scrapy_parser_pep
```  
  
Cоздать и активировать виртуальное окружение:  
  
```  
python3 -m venv env  
```  
  
```  
source env/bin/activate  
```  
  
Установить зависимости из файла requirements.txt:  
  
```  
python3 -m pip install --upgrade pip  
```  
  
```  
pip install -r requirements.txt  
```

## Команды запуска/Справка

### Справка

```bash
scrapy -h
```

```
Scrapy 2.5.1 - project: pep_parse

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  commands      
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

Use "scrapy <command> -h" to see more info about a command


```

### Пример выполнения команды

**Команда:**

```bash
scrapy crawl pep
```

**Результат:**

В директории ***scrapy_parser_pep/results*** должны появиться два файла:

```bash
(venv) .../scrapy_parser_pep/results$ ls
pep_2024-08-16T06-58-15.csv  status_summary_2024-08-16_09-58-25.csv

```

Содержимое файла *pep_2024-08-16T06-58-15.csv*:

```
number,name,status  
1,PEP Purpose and Guidelines,Active  
11,CPython platform support,Active  
10,Voting Guidelines,Active  
602,Annual Release Cycle for Python,Active  
729,Typing governance process,Active
...
```

Содержимое файла *status_summary_2024-08-16_09-58-25.csv*:

```
Статус,Количество  
Active,33  
Final,315  
Draft,34  
Superseded,23  
Deferred,35  
Rejected,124  
Withdrawn,61  
April Fool!,1  
Accepted,22  
Provisional,2  
Общее количество,650
```
