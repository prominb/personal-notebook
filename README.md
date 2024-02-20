# Проект "Імплементація боту та сортування файлів"

Цей проект містить бота для управління адресною книгою, управління нотатками та інструмент для автоматичного сортування файлів.

## Вміст

1. [Структура проекту](#структура-проекту)
2. [Опис](#опис)
3. [Встановлення](#встановлення)
4. [Використання](#використання)

<a name='структура-проекту'></a>

### Структура проекту

├── bot.py  
├── main.py  
├── notes.py  
├── sorted.py  
├── colors.py  
└── classes.py

packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│ └── example_package_YOUR_USERNAME_HERE/
│ ├── **init**.py
│ └── example.py
└── tests/

<a name='опис'></a>

## Опис

### bot.py

Файл `bot.py` містить реалізацію бота для управління адресною книгою.

### main.py

Головний файл `main.py`, який запускає бота.

### notes.py

Модуль `notes.py` містить функції для роботи з нотатками, такі як додавання, редагування та видалення.

### sorted.py

У файлі `sorted.py` реалізовано інструмент для сортування файлів за категоріями.

### colors.py

У файлі `colors.py` визначені константи для кольорів консольного виведення.

### classes.py

Модуль `classes.py` включає в себе класи для роботи з контактами та адресною книгою.

<a name='встановлення'></a>

## Встановлення

1. Завантажте код проекту на свій комп'ютер.
2. Відкрийте термінал або командний рядок у каталозі проекту.
3. Використовуйте команду `pip install -r requirements.txt`, щоб встановити залежності.

<a name='використання'></a>

## Використання

### Запуск бота

Використовуйте команду:
`python main.py`

Після запуску ви побачите команди:

- **hello** - Вивести привітальне повідомлення.
- **add** - Додати новий контакт. Потрібно вказати ім'я та інші дані.
- **change** - Змінити ім'я контакту. Потрібно вказати старе та нове ім'я.
- **phone** - Змінити телефонний номер контакту. Потрібно вказати ім'я та новий номер.
- **email** - Змінити електронну пошту контакту. Потрібно вказати ім'я та нову пошту.
- **show all** - Показати всі доступні контакти.
- **search** - Пошук контакту за ім'ям чи номером телефону.
- **good bye, close, exit** - Вийти з програми.
- **sorted** - Сортувати файли в папці.
- **notes** - Запустити функціонал для роботи з нотатками.

### Сортування файлів

Використовуйте команду:
`python sorted.py Шлях_до_папки`

### Вийнятки та Керування Помилками

Бот має вбудовану систему виправлення помилок, тому слід слідкувати за виведеними повідомленнями та дотримуватися вказівок.

**Тепер ви готові використовувати бота! Бажаємо вам приємного користування та успішної роботи з вашим проектом.**
