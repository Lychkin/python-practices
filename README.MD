Набор практических работ по курсу "ВПК-8. Разработка прикладных решений на языке Python, 2025"

## Установка

### Предварительные требования
*   Python 3.5 или выше
*   pip (обычно идет в комплекте с Python)

### 1. Клонирование репозитория
```bash
git clone https://github.com/Lychkin/python-practices.git
cd your-repo
```

### 2. Создание виртуального окружения (рекомендуется)
```bash
python -m venv venv
# Для Linux/macOS:
source venv/bin/activate
# Для Windows:
.\venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск практических работ

Каждая практическая работа находится в отдельной папке (`practice_01`, `practice_02` и т.д.). Для запуска необходимо перейти в соответствующую папку и выполнить нужный Python-файл.

### Пример запуска работы №1:
```bash
cd practice_01
python main.py
```
### Запуск проверки PEP8

```bash
# Проверить конкретный файл
flake8 practice_01/main.py

# Проверить все файлы в проекте
flake8 .

# Проверить конкретную практическую работу
flake8 practice_02/
```