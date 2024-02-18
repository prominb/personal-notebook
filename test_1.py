import re
import shutil
import sys
from pathlib import Path

# Функция normalize
def normalize(filename):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    normalize_filename = filename.translate(TRANS)  # транслітерація
    normalize_filename = re.sub(r'[^A-Za-z0-9.]+', "_", normalize_filename)  # заміна не літер та не цифр на симовл "_"
    return normalize_filename

# створимо порожні списки файлів, до яких будемо відправляти назви файлів
image_files = []
document_files = []
audio_files = []
video_files = []
archive_files = []
known_ext = []  # перелік відомих розширень
unknown_ext = []  # перелік невідомих розширень

# Список папок, які ігнорує скрипт, та до яких будемо додавати файли:
target_folders = ['archives', 'video', 'audio', 'documents', 'images']

# Створюємо папки зі списку target_folders
def create(folder_path):
    for folder in target_folders:
        new_folder_path = folder_path / folder
        new_folder_path.mkdir(exist_ok=True, parents=True)
    return None

# Перевіримо папки на наповнення та видалимо порожні
def clear(folder_path):
    for folder in folder_path.iterdir():
        if folder.is_dir():
            if folder.name not in target_folders:
                if folder.stat().st_size == 0:
                    folder.rmdir()
    return None

# Функція, що перебирає файли, сортує їх по папкам
def main_sorted_folder(folder_path):
    # визначаємо розширення за якими будемо сортувати файли
    image_ext = ['JPEG', 'PNG', 'JPG', 'SVG']
    document_ext = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
    audio_ext = ['MP3', 'OGG', 'WAV', 'AMR']
    video_ext = ['AVI', 'MP4', 'MOV', 'MKV']
    archive_ext = ['ZIP', 'GZ', 'TAR']

    # якщо це папка, рекурсивно ходимо по папкам
    for element in folder_path.iterdir():
        if element.is_dir() and element not in target_folders:
            main_sorted_folder(element)
        else:
            for file in folder_path.iterdir():
                if file.suffix[1:].upper() in image_ext:
                    image_folder = Path('images')
                    file.replace(folder_path / image_folder / normalize(file.name))
                    known_ext.append(file.suffix)
                    image_files.append(normalize(file.name))
                elif file.suffix[1:].upper() in document_ext:
                    document_folder = Path('documents')
                    file.replace(folder_path / document_folder / normalize(file.name))
                    known_ext.append(file.suffix)
                    document_files.append(normalize(file.name))
                elif file.suffix[1:].upper() in audio_ext:
                    audio_folder = Path('audio')
                    file.replace(folder_path / audio_folder / normalize(file.name))
                    known_ext.append(file.suffix)
                    audio_files.append(normalize(file.name))
                elif file.suffix[1:].upper() in video_ext:
                    video_folder = Path('video')
                    file.replace(folder_path / video_folder / normalize(file.name))
                    known_ext.append(file.suffix)
                    video_files.append(normalize(file.name))
                elif file.suffix[1:].upper() in archive_ext:
                    archive_folder = Path('archives')
                    file.replace(folder_path / archive_folder / normalize(file.name))
                    known_ext.append(file.suffix)
                    archive_files.append(normalize(file.name))
                else:
                    normalize(file.name)
                    if not file.is_dir():
                        unknown_ext.append(file.suffix)
    return None

# Створюємо функцію, яка буде розпаковувати архівні файли у папки з тією ж назвою
def archive_folder(folder_path):
    archive_path = folder_path / 'archives'
    for file in archive_path.iterdir():
        new_folder_path = archive_path / file.stem
        new_folder_path.mkdir(exist_ok=True, parents=True)
        shutil.unpack_archive(str(file), str(new_folder_path))
    return None

def clean():
    sort_folder = sys.argv[1]
    sort_folder = Path(sys.argv[1])    
    create(sort_folder)
    main_sorted_folder(sort_folder)
    clear(sort_folder)
    archive_folder(sort_folder)

if __name__ == '__main__':
    clean()