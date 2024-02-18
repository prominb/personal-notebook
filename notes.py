import json
from colors import *


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=2)


def add_note():
    title = input("Введіть заголовок нотатки: ")
    content = input("Введіть текст нотатки: ")
    tags = input("Введіть теги (через пробіл): ").split()
    
    notes = load_notes()
    notes.append({'title': title, 'content': content, 'tags': tags})
    save_notes(notes)
    print("Нотатка додана успішно!")


def search_notes(query):
    notes = load_notes()
    found_notes = [note for note in notes if query in note['title'] or query in note['content'] or query in note['tags']]
    
    if found_notes:
        print("Знайдені нотатки:")
        for note in found_notes:
            display_note(note['title'])
            print("---")
    else:
        print("Нотаток не знайдено.")


def filter_by_tag(tag):
    notes = load_notes()
    filtered_notes = [note for note in notes if tag in note['tags']]

    if filtered_notes:
        print(f"Нотатки з тегом '{tag}':")
        for note in filtered_notes:
            display_note(note['title'])
            print("---")
    else:
        print(f"Нотаток з тегом '{tag}' не знайдено.")


def edit_note():
    notes = load_notes()
    title_to_edit = input("Введіть заголовок нотатки, яку ви хочете відредагувати: ")

    for note in notes:
        if note['title'] == title_to_edit:
            print(f"Знайдено нотатку з заголовком '{title_to_edit}'.")
            new_title = input("Введіть новий заголовок (або залиште порожнім, щоб залишити без змін): ")
            new_content = input("Введіть новий текст (або залиште порожнім, щоб залишити без змін): ")
            new_tags = input("Введіть нові теги (через пробіл, або залиште порожнім, щоб залишити без змін): ").split()

            note['title'] = new_title if new_title else note['title']
            note['content'] = new_content if new_content else note['content']
            note['tags'] = new_tags if new_tags else note['tags']

            save_notes(notes)
            print("Нотатка відредагована успішно!")
            return

    print(f"Нотатка з заголовком '{title_to_edit}' не знайдена.")


def delete_note():
    notes = load_notes()
    title_to_delete = input("Введіть заголовок нотатки, яку ви хочете видалити: ")

    for note in notes:
        if note['title'] == title_to_delete:
            notes.remove(note)
            save_notes(notes)
            print(f"Нотатка з заголовком '{title_to_delete}' видалена успішно!")
            return

    print(f"Нотатка з заголовком '{title_to_delete}' не знайдена.")

def display_note(title):
    notes = load_notes()

    for note in notes:
        if note['title'] == title:
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['content']}")
            print(f"Теги: {', '.join(note['tags'])}")
            return

    print(f"Нотатка з заголовком '{title}' не знайдена.")

def main():
    while True:
        print(f"{GREEN}\n1. Додати нотатку")
        print(f"2. Пошук нотаток")
        print(f"3. Редагувати нотатку")
        print(f"{RED}4. Видалити нотатку{DEFALUT}")
        print(f"{GREEN}5. Вивести нотатку в консоль")
        print(f"6. Фільтрувати нотатки за тегом")
        print(f"{RED}7. Вийти{DEFALUT}")
        
        choice = input("Введіть номер опції: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            query = input("Введіть запит для пошуку: ")
            search_notes(query)
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            title_to_display = input("Введіть заголовок нотатки для виведення в консоль: ")
            display_note(title_to_display)
        elif choice == '6':
            tag_to_filter = input("Введіть тег для фільтрації нотаток: ")
            filter_by_tag(tag_to_filter)
        elif choice == '7':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
