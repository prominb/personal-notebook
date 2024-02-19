from classes import Record, AddressBook
from datetime import datetime, timedelta
from colors import *
from comands import *
import json
import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.input import win32 as win32_input
from sorted import *
from notes import run_notes


class InputError(Exception):
    pass


class ContactAssistant:

    def __init__(self):
        # self.upcoming_birthdays = []  # Змінено на екземпляр атрибуту
        self.address_book = AddressBook()
        self.file_path = "contacts.json"

        if os.path.exists(self.file_path):
            self.load_data()

    def save_data(self):
        with open(self.file_path, "w") as file:
            data = {
                "records": [record.__json__() for record in self.address_book.values()]
            }
            json.dump(data, file, indent=2)  # Установите indent=2 для форматированного вывода с отступами

    def load_data(self):
        try:
            if os.path.getsize(self.file_path) > 0:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    for record_data in data.get("records", []):
                        name = record_data.get("name")
                        birthday = record_data.get("birthday")
                        address = record_data.get("address")
                        record = Record(name, birthday=birthday, address=address)
                        
                        phones = record_data.get("phones", [])
                        for phone in phones:
                            record.add_phone(phone)
                        
                        emails = record_data.get("emails", [])
                        for email in emails:
                            record.add_email(email)
                        
                        self.address_book.add_record(record)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Помилка завантаження даних: {e}")

    def add_contact(self, name, **args):
        try:
            record = Record(name)
            for arg, val in args.items():
                if arg == 'phone':
                    record.add_phone(val)
                elif arg == 'email':
                    record.add_email(val)
                elif arg == 'birthday':
                    record.set_birthday(val)
                elif arg == 'address':
                    record.set_address(val)
            self.address_book.add_record(record)
            self.save_data()
            return f"{YLLOW}Новий контакт успішно доданий!!!{PISKAZKA_SHOW_ALL}"
        except ValueError as e:
            raise InputError(str(e))

    def change_contact(self, name, phone=None, email=None, address=None, birthday=None):
        try:
            record = self.address_book.find(name)
            if record:
                if phone:
                    record.phones = []
                    record.add_phone(phone)
                if email:
                    record.emails = []
                    record.add_email(email)
                if address:
                    record.set_address(address)
                if birthday:
                    record.set_birthday(birthday)
                self.save_data()
                return f"{YLLOW}Дані успішно змінені!!!{PISKAZKA_SHOW_ALL}"
            else:
                raise IndexError(f"{YLLOW}Не знайдено контакт {BIRUZA}{name}{DEFALUT}! {PISKAZKA_SHOW_ALL}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def get_email(self, name, emails):
        try:
            record = self.address_book.find(name)
            if record and record.emails:
                emails = ', '.join(str(email) for email in record.emails)
                return f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено email{BIRUZA} {emails}{DEFALUT}"
            else:
                raise IndexError(f"{YLLOW}Такого імені або email не знайдено у вашій телефоній книзі !!!"
                                 f"{DEFALUT}{PISKAZKA_SHOW_ALL} ")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def add_email_to_contact(self, name, email):
        try:
            record = self.address_book.find_case_insensitive(name)
            if record:
                record.add_email(email)
                self.save_data()
                print(f"DEBUG: Email успешно добавлен для контакта {record.name.value} - {email}")
                return f"{YLLOW}Email успешно додано для контакта {BIRUZA}{record.name.value}{DEFALUT}"
            else:
                raise IndexError(f"{YLLOW}Такого імені не знайдено у вашій телефоній книзі !!!"
                                 f"{DEFALUT}{PISKAZKA_SHOW_ALL}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))
        
    def get_email_by_email(self, email):
        try:
            return self.get_email(email)
        except InputError:
            raise InputError(f"{YLLOW}Такого імені або email не знайдено у вашій телефоній книзі !!!"
                             f"{DEFALUT}{PISKAZKA_SHOW_ALL}")

    def get_phone(self, name):
        try:
            record = self.address_book.find(name)
            if record:
                return (f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено номер"
                        f"{BIRUZA} {record.phones[0]}{DEFALUT}")
            else:
                raise IndexError(f"{YLLOW}Такого іменні не знайдено у вашій телефоній книзі !!!"
                                 f"{DEFALUT}{PISKAZKA_SHOW_ALL} ")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def show_all_contacts(self):
        records = list(self.address_book.values())
        if not records:
            return f"{YLLOW}Ваша телефонна книга поки не містить жодного конткту{DEFALUT}"
        else:
            result = f'{GREEN}{"Name":<10} {"Birthday":^12} {"Phone":<12} {"Email":<20} {"Address":<20} {YLLOW}\n'
            for record in records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                emails = ', '.join(map(str, [email.value for email in record.emails if email.value]))
                result += (f"{record.name.value:<10} {str(record.birthday):^12} {phone_numbers:<12}"
                           f" {emails:<20} {str(record.address):<20}\n")

            return result.strip()   


class CommandHandler:
    
    def __init__(self, contact_assistant):
        self.contact_assistant = contact_assistant

    def handle_hello(self, **args):
        return f"{YLLOW}How can I help you?{DEFALUT}"

    def handle_add(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_ADD)
        contact_info = args.split(" ")
        if len(contact_info) < 3:
            raise InputError(BAD_COMMAND_ADD)

        _, name, *contact_values = contact_info
        
        phone = None
        email = None
        address = None
        birthday = None

        for contact_value in contact_values:
            parameter, val = contact_value.split('=')
            if parameter.strip() == 'email':
                email = val.strip()
            elif parameter.strip() == 'phone':
                phone = val.strip()
            elif parameter.strip() == 'address':
                address = val.strip()
            elif parameter.strip() == 'birthday':
                birthday = val.strip()
            else:
                raise InputError(BAD_COMMAND_ADD)

        try:
            return self.contact_assistant.add_contact(name=name, phone=phone, email=email,
                                                      address=address, birthday=birthday)
        except InputError as e:
            raise InputError(str(e))

    def handle_change(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_CHANGE)

        contact_info = args.split(" ")
        if len(contact_info) != 3:
            raise InputError(BAD_COMMAND_CHANGE)

        _, name, contact_value = args.split(" ")
        print(contact_value)
        parameter, val = contact_value.split('=')
        if parameter.strip() == 'email':
            return self.contact_assistant.change_contact(name, email=val.strip())
        elif parameter.strip() == 'phone':
            return self.contact_assistant.change_contact(name, phone=val.strip())
        elif parameter.strip() == 'address':
            return self.contact_assistant.change_contact(name, address=val.strip())
        elif parameter.strip() == 'birthday':
            return self.contact_assistant.change_contact(name, birthday=val.strip())
        else:
            raise InputError(BAD_COMMAND_CHANGE)

    def handle_email(self, args):
        if len(args.split()) < 2:
            raise InputError("BAD_COMMAND_EMAIL")

        name_or_email, *emails = args.split(" ", 1)[1].strip().split(",")
        
        if '@' in name_or_email:
            return self.contact_assistant.get_email_by_email(name_or_email.strip())
        return self.contact_assistant.get_email(name_or_email)

    def handle_phone(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_PHONE)
        args_list = args.split(" ")
        name = args_list[1]
        return self.contact_assistant.get_phone(name)

    def handle_show(self, args):
        return self.contact_assistant.show_all_contacts()

    def handle_bye(self, args):
        print("До побачення!")
        return None

    def handle_birthdays(self, args):
        try:
            if len(args.split()) < 2:
                raise InputError(BAD_COMMAND_BIRTHDAYS)

            _, days = args.split(" ", 1)
            days = int(days)

            result = self.contact_assistant.birthdays_in_days(days)
            if not result:
                return f"{YLLOW}Немає жодних днів народження наступні {days} днів.{DEFALUT}"
            else:
                output = f"{YLLOW}Найближчі дні народження протягом наступних {days} днів:{DEFALUT}\n"
                for name, days_until_birthday in result:
                    output += f"{BIRUZA}{name}{DEFALUT} - {RED}{days_until_birthday}{DEFALUT} днів\n"
                return output.strip()

        except (IndexError, ValueError):
            raise InputError(BAD_COMMAND_BIRTHDAYS)
    
    def handle_search(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_SEARCH)

        query = args.split(" ", 1)[1]
        matching_records = self.contact_assistant.address_book.search(query)

        if not matching_records:
            return f"{YLLOW}Нажаль нічого не знайдено  {DEFALUT}"
        else:
            result = f"{YLLOW}За Вашим запитом = {RED}{query}{YLLOW} було знайдено наступні записи :{DEFALUT}\n"
            for record in matching_records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                result += f"{record.name}: {phone_numbers}\n"
            return result.strip()    
    
    def handle_sorted(self, args):
        try:
            if len(args.split()) < 2:
                raise InputError(BAD_COMMAND_SORTED)

            folder_path = args.split(" ")[1]
            result = main(folder_path)  # Вызываем функцию clean() и сохраняем результат
            return result  # Возвращаем результат выполнения функции clean()
        except InputError as e:
            raise e 
    
    def handle_notes(self, args):
        run_notes()

    def choice_action(self, data):
        actions = {
            'hello': self.handle_hello,
            'add': self.handle_add,
            "change": self.handle_change,
            "phone": self.handle_phone,
            'search': self.handle_search,
            'email': self.handle_email,
            "show": self.handle_show,
            "birthday": self.handle_birthdays,  # Додано обробку команди "birthday"
            "close": self.handle_bye,
            "exit": self.handle_bye,
            "good bye": self.handle_bye,
            'sorted': self.handle_sorted,
            'notes': self.handle_notes,
        }
        return actions.get(data, lambda args: f'{YLLOW}Така команда не підтримується наразі\n'
                                              f'{DEFALUT}{DOSTUPNI_COMANDY}')

    def process_input(self, user_input):
        try:
            if not user_input:
                raise InputError(f'{YLLOW}Ви нічого не ввели \n{DOSTUPNI_COMANDY}')

            space_index = user_input.find(' ')

            if space_index != -1:
                first_word = user_input[:space_index]
            else:
                first_word = user_input

            if first_word in ["good", "bye"]:
                first_word = "good bye"

            func = self.choice_action(first_word)
            result = func(user_input)

            if result is None:
                return None
            else:
                return result
        except InputError as e:
            return str(e)


class Bot:

    def run(self):
        print(f'\n{YLLOW}Вас вітає Бот для роботи з вашии контактами.')
        print(f'{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT + ["birthday"]}{DEFALUT}')
        contact_assistant = ContactAssistant()
        command_handler = CommandHandler(contact_assistant)
        # Список вариантів для автодоповнення
        # words = ['hello', 'help', 'add', 'change', 'phone', 'show all', 'search', 'good bye', 'close',
        # 'exit', 'sorted', 'notes']

        # Створюємо комплиттер з нашими варінтами
        completer = WordCompleter(LIST_COMANDS_BOT, ignore_case=True)

        while True:
            try:

                user_input = prompt("Введіть команду>> ", completer=completer).lower().strip()
                
                result = command_handler.process_input(user_input)

                if result is None:
                    break
                else:
                    print(result)

            except Exception as e:
                print(e)
