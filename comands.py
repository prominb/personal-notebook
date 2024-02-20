from colors import * 
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["hello", "add", "show all", "change", 'search', "get phone", "email", 'birthday', 'sorted', 'notes', "exit"]
# LIST_COMANDS_BOT = ["hello", "add", "change", "phone", "email", "show all", 'search', "good bye", "close", "exit",
#                     'sorted', 'notes']
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
PATH_TO_DIR = fr"C:\Users\User\Desktop\Go_IT\Rizne"

BAD_COMMAND_ADD = f"{YLLOW}Невірні параметри для команди {GREEN}'add'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту{YLLOW} Номер_телефону|Еmail {DEFALUT}"
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}'change'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту {GREEN}name {BIRUZA} Нове ім'я "
    
BAD_COMMAND_PHONE = f"{YLLOW}Невірні параметри для команди {GREEN}'get phone'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}get phone{BIRUZA} Andrew  {RED}<<{GREEN} get phone {YLLOW}'Імя контакту'{RED} >> "
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}'search'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} Імя_контакту{YLLOW} "

BAD_COMMAND_SORTED = f"{YLLOW}Невірні параметри для команди {GREEN}'sorted'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}sorted{BIRUZA} {PATH_TO_DIR}  {RED}<<{GREEN} sorted {BIRUZA}'Шлях до папки'{RED} >>"

BAD_COMMAND_NOTES = f"{YLLOW}Невірні параметри для команди {GREEN}'notes'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}notes"
BAD_COMMAND_EMAIL = f"{YLLOW}Невірні параметри для команди {GREEN}'email'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}'email'{BIRUZA}"

BAD_COMMAND_BIRTHDAYS = f"{YLLOW}Невірні параметри для команди {GREEN}'birthday'{YLLOW} !!!.\n\
                {RED}# Приклад:  {GREEN}birthday{YLLOW} 50  {RED}<<{GREEN} birthday {YLLOW}'кількість днів'{RED} >>"


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BAD_FORMAT_PHONE = (f"{RED}Невірний формат !!!{YLLOW}<Номер може містити тільки 10 цифри !!!>\n{GREEN}\
                    ### Приклад:  0931245891{DEFALUT}")

BAD_FORMAT_EMAIL = f"{YLLOW}Не вірний формат e-mail.\n {RED}Приклад - {BIRUZA}python@gmail.com"

BAD_FORMAT_BIRTHDAY = f"{YLLOW}Не вірний формат дати народження. Використовуйте {RED}YYYY-MM-DD."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

NOT_FOUND_NAME = f"{YLLOW}Такого імені не знайдено у вашій телефоній книзі !!!\n {PISKAZKA_SHOW_ALL}"

NOT_FOUND_COMMAND = f'{YLLOW}Tака команда не пітримується наразі\n{DEFALUT}{DOSTUPNI_COMANDY}'


