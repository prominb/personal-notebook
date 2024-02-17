from classes import Record, AddressBook
from colors import *
from comands import *
import json
import os

class InputError(Exception):
    pass

class ContactAssistant:
   
    
    def __init__(self):
        self.address_book = AddressBook()
        self.file_path = "contacts.json"
       
        if os.path.exists(self.file_path):
            self.load_data()

    def save_data(self):
        with open(self.file_path, "w") as file:
            data = {
                "records": [record.__json__() for record in self.address_book.values()]
            }
            json.dump(data, file)

    def load_data(self):
        try:
            if os.path.getsize(self.file_path) > 0:  
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    records = [Record(record["name"], record.get("birthday")) for record in data.get("records", [])]
                    for i, record in enumerate(records):
                        if "phones" in data.get("records", [])[i]:
                            for phone in data["records"][i]["phones"]:
                                record.add_phone(phone)
                        self.address_book.add_record(record)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading data: {e}")


    def add_contact(self, name, phone=None, email=None, birthday=None):
        try:
            record = Record(name, birthday)
            if phone:
                record.add_phone(str(phone).strip())
            if email:
                record.add_email(str(email).strip())
            self.address_book.add_record(record)
            self.save_data()
            return f"{YLLOW}New contact successfully added!!!{PISKAZKA_SHOW_ALL}"
        except ValueError as e:
            raise InputError(str(e))

    def change_contact(self, name, phone=None, email=None):
        try:
            record = self.address_book.find(name)
            if record:
                if phone:
                    if len(phone) == 10 and phone.isdigit():
                        record.phones = []
                        record.add_phone(phone)
                    else:
                        raise ValueError(f"{YLLOW}Phone number can only contain 10 digits!!!{BIRUZA}\n# Example - 0931245891")
                if email:
                    record.emails = []
                    record.add_email(email)
                self.save_data()
                return f"{YLLOW}Phone number/email successfully changed!!!{PISKAZKA_SHOW_ALL}"
            else:
                raise IndexError(f"{YLLOW}No entry found with the name {BIRUZA}{name}{DEFALUT}{PISKAZKA_SHOW_ALL}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def get_email(self, name):
        try:
            record = self.address_book.find(name)
            if record and record.emails:
                emails = ', '.join(str(email) for email in record.emails)
                return f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено email{BIRUZA} {emails}{DEFALUT}"
            else:
                raise IndexError(f"{YLLOW}Такого імені або email не знайдено у вашій телефоній книзі !!!{DEFALUT}{PISKAZKA_SHOW_ALL} ")
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
                raise IndexError(f"{YLLOW}Такого імені не знайдено у вашій телефоній книзі !!!{DEFALUT}{PISKAZKA_SHOW_ALL}")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def get_phone(self, name):
        try:
            record = self.address_book.find(name)
            if record:
                return f"{YLLOW}За вказаним іменем {BIRUZA}{name}{YLLOW} знайдено номер{BIRUZA} {record.phones[0]}{DEFALUT}"
            else:
                raise IndexError(f"{YLLOW}Такого іменні не знайдено у вашій телефоній книзі !!!{DEFALUT}{PISKAZKA_SHOW_ALL} ")
        except (ValueError, IndexError) as e:
            raise InputError(str(e))

    def show_all_contacts(self):
        records = list(self.address_book.values())
        if not records:
            return f"{YLLOW}Ваша телефона книга поки не містить жодного запису{DEFALUT}"
        else:
            result = f'{GREEN}{"Name":<10}  {"Phone":<12} {"Email":<20}{YLLOW}\n'
            for record in records:
                phone_numbers = ', '.join(str(phone) for phone in record.phones)
                emails = ', '.join(str(email.value) if email.value else '' for email in record.emails)
                result += f"{record.name}  {phone_numbers}  {emails}\n" 
            return result.strip()

    

class CommandHandler:
    
    
    def __init__(self, contact_assistant):
        self.contact_assistant = contact_assistant

    def handle_hello(self, args):
        return f"{YLLOW}How can I help you?{DEFALUT}"

    def handle_add(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_ADD)

        contact_info = args.split(" ")
        if len(contact_info) not in [3, 4]:
            raise InputError(BAD_COMMAND_ADD)

        _, name, contact_value = args.split(" ")
        if "@" in contact_value:
            return self.contact_assistant.add_contact(name, email=contact_value)
        elif contact_value.isdigit():
            return self.contact_assistant.add_contact(name, phone=contact_value)
        else:
            raise InputError(BAD_COMMAND_ADD)

    def handle_change(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_CHANGE)

        contact_info = args.split(" ")
        if len(contact_info) != 3:
            raise InputError(BAD_COMMAND_CHANGE)

        _, name, contact_value = args.split(" ")
        if "@" in contact_value:
            return self.contact_assistant.change_contact(name, email=contact_value)
        elif contact_value.isdigit():
            return self.contact_assistant.change_contact(name, phone=contact_value)
        else:
            raise InputError(BAD_COMMAND_CHANGE)

    def handle_email(self, args):
        if len(args.split()) < 2:
            raise InputError("BAD_COMMAND_EMAIL")

        name, *emails = args.split(" ", 1)[1].strip().split(",")
        for email in emails:
            self.contact_assistant.add_email_to_contact(name, email.strip())

        return self.contact_assistant.get_email(name)

    def handle_phone(self, args):
        if len(args) == 0:
            raise InputError(BAD_COMMAND_PHONE)
        args_list = args.split(" ")
        name = args_list[1]
        return self.contact_assistant.get_phone(name)

    def handle_show(self, args):
        return self.contact_assistant.show_all_contacts()

    def handle_bye(self, args):
        print("Good bye!")
        return None
    
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

    def choice_action(self, data):
        actions = {
            'hello': self.handle_hello,
            'add': self.handle_add,
            "change": self.handle_change,
            "phone": self.handle_phone,
            'search': self.handle_search,
            'email': self.handle_email,
            "show": self.handle_show,
            "close": self.handle_bye,
            "exit": self.handle_bye,
            "good bye": self.handle_bye,
        }
        return actions.get(data, lambda args: f'{YLLOW}Така команда не підтримується наразі\n{DEFALUT}{DOSTUPNI_COMANDY}')


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
    
    
    print(f'\n{YLLOW}Вас вітає Бот для роботи з вашии контактами.')
    print(f'{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}')
    
    def run(self):
        contact_assistant = ContactAssistant()
        command_handler = CommandHandler(contact_assistant)

        while True:
            try:
                user_input = input(f"{PURPURE}Ведіть команду>>{DEFALUT}").lower().strip()
                result = command_handler.process_input(user_input)

                if result is None:
                    break
                else:
                    print(result)

            except Exception as e:
                print(e)


