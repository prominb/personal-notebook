from colors import * 
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["help", "hello", "add", "phone", "email", "show all", "change", 'search',
                    "good bye", "close", "exit", 'sorted', 'notes', 'birthday']
# LIST_COMANDS_BOT = ["hello", "add", "change", "phone", "email", "show all", 'search', "good bye", "close", "exit",
#                     'sorted', 'notes']
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
PATH_TO_DIR = fr"C:\Users\User\Desktop\Go_IT\Rizne"

BAD_COMMAND_ADD = f"{YLLOW}Невірні параметри для команди {GREEN}add{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту{YLLOW} Номер_телефону|Еmail {DEFALUT}"
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}change{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту {GREEN}name {BIRUZA} Нове ім'я "
    
BAD_COMMAND_PHONE = f"{YLLOW}Невірні параметри для команди {GREEN}phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}phone{BIRUZA} Імя_контакту{YLLOW} "
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}search{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} Імя_контакту{YLLOW} "

BAD_COMMAND_SORTED = f"{YLLOW}Невірні параметри для команди {GREEN}sorted{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}sorted{BIRUZA} {PATH_TO_DIR}\n"

BAD_COMMAND_NOTES = f"{YLLOW}Невірні параметри для команди {GREEN}notes{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}notes{BIRUZA}"

BAD_COMMAND_BIRTHDAYS = f"{YLLOW}Невірні параметри для команди {GREEN}phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}phone{BIRUZA} Імя_контакту{YLLOW} "

BAD_COMMAND_EMAIL = f"{YLLOW}Невірні параметри для команди {GREEN}email{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}email{BIRUZA} Імя_контакту{YLLOW} "

HELP = f" {GREEN}Довідка для Контактного Асистента\n{DEFALUT}" \
                f"{YLLOW}======================================================={DEFALUT}\n" \
                f"{GREEN}Вітаємо у Контактному Асистенті! Ця програма допомагає ефективно керувати вашими контактами.{DEFALUT}\n" \
                f"Список доступних команд:\n" \
                f"{BIRUZA}- `hello`: Привітати бота.\n" \
                f"- `add name phone=<номер_телефону> email=<адреса_електронної_пошти> birthday=<РРРР-ММ-ДД> address=<адреса>`: Додати новий контакт.{DEFALUT}\n" \
                f"  - Приклад: `add Іван Петров phone=1234567890 email=ivan@example.com birthday=1990-01-01 address=вул. Головна, 1`{DEFALUT}\n" \
                f"  - Примітка: Поля `phone`, `email`, `birthday`, та `address` є опціональними, і ви можете вказати тільки ті, які необхідно.{DEFALUT}\n" \
                f"  - Приклад неправильного введення: `add Іван Петров phone=1234 email=ivan@example.com birthday=1990-01-01 address=вул. {DEFALUT}\n" \
                f"    Головна, 1` (невірний номер телефону).{DEFALUT}\n" \
                f"- `change name <ім'я_контакту> <поле_для_зміни>=<нове_значення>`: Змінити деталі контакту.{DEFALUT}\n" \
                f"  - Приклад: `change Іван Петров email=newemail@example.com`{DEFALUT}\n" \
                f"- `phone name <ім'я_контакту>`: Отримати номер телефону контакту.{DEFALUT}\n" \
                f"  - Приклад: `phone Іван Петров`{DEFALUT}\n" \
                f"- `search <запит>`: Пошук контактів за ім'ям, номером телефону, електронною поштою чи адресою.{DEFALUT}\n" \
                f"  - Приклад: `search Іван`{DEFALUT}\n" \
                f"- `email <ім'я_контакту або email>`: Отримати адресу електронної пошти контакту.{DEFALUT}\n" \
                f"  - Приклад: `email ivan@example.com`{DEFALUT}\n" \
                f"- `show`: Показати всі контакти в телефонній книзі.{DEFALUT}\n" \
                f"  - Приклад: `show`{DEFALUT}\n" \
                f"- `birthday <дні>`: Показати найближчі дні народження протягом вказаної кількості днів.{DEFALUT}\n" \
                f"  - Приклад: `birthday 7`{DEFALUT}\n" \
                f"- `close`, `exit`, `good bye`: Вийти з програми.{DEFALUT}\n" \
                f"  - Приклад: `close`, `exit`, `good bye`{DEFALUT}\n" \
                f"- `sorted <шлях_до_папки>`: Впорядкувати файли у вказаній папці.{DEFALUT}\n" \
                f"  - Приклад: `sorted /шлях/до/папки`{DEFALUT}\n" \
                f"- `notes`: Відкрити функціонал заміток.{DEFALUT}\n" \
                f"  - Приклад: `notes`{DEFALUT}\n" \
                f"    Вітаємо у Контактному Асистенті! Асистент допомагає ефективно керувати вашими нотатками.{DEFALUT}\n" \
                f"    Список доступних команд:{DEFALUT}\n" \
                f"    - `1`: Додати нову нотатку.{DEFALUT}\n" \
                f"       - Приклад: Введіть `1` для додавання нової нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"    - `2`: Пошук нотаток за заголовком чи змістом.{DEFALUT}\n" \
                f"       - Приклад: Введіть `2` та введіть запит для пошуку (заголовок чи зміст).{DEFALUT}\n" \
                f"    - `3`: Редагувати існуючу нотатку.{DEFALUT}\n" \
                f"       - Приклад: Введіть `3` для редагування існуючої нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"    - `4`: Видалити нотатку.{DEFALUT}\n" \
                f"      - Приклад: Введіть `4` для видалення нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"    - `5`: Вивести всі нотатки в консоль.{DEFALUT}\n" \
                f"       - Приклад: Введіть `5` для виведення всіх нотаток в консоль.{DEFALUT}\n" \
                f"    - `6`: Вивести нотатку за заголовком.{DEFALUT}\n" \
                f"       - Приклад: Введіть `6` для виведення конкретної нотатки за заголовком.{DEFALUT}\n" \
                f"    - `7`: Вивести нотатку(-и) за тегом.{DEFALUT}\n" \
                f"       - Приклад: Введіть `7` для виведення нотаток за певним тегом.{DEFALUT}\n" \
                f"    - `8`: Вивести нотатки за певними тегами у вигляді таблиці.{DEFALUT}\n" \
                f"       - Приклад: Введіть `8` для виведення нотаток за певними тегами у вигляді таблиці.{DEFALUT}\n" \
                f"    - `9`: Вийти з програми.{DEFALUT}\n" \
                f"       - Приклад: Введіть `9` для виходу з програми.  {DEFALUT}\n" \
                f"Примітка: Використовуйте подвійні лапки для значень, що містять пробіли.{DEFALUT}\n" \
                f"Бажаємо вам приємного користування Контактним Асистентом!{DEFALUT}\n" 
