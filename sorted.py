import sys
from pathlib import Path
import uuid
import shutil


CYRILLIC_SYMBOLS = "абвгґдеёєжзиіїйклмнопрстуфхцчшщъыьэюя"
TRANSLATION = ("a", "b", "v", "h", "g", "d", "e", "e", "ie" "zh", "z",
               "y", "i", "yi", "y", "j", "k", "l", "m", "n", "o", "p",
               "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch",
               "", "y", "", "e", "yu", "ya")

# Список запрещенных символов
BAD_SYMBOLS = ("%", "*", " ", "-")

# Словарь для трансляции запрещенных и кириллических символов
TRANS = {}
for c, t in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()

for i in BAD_SYMBOLS:
    TRANS[ord(i)] = "_"


# Функция для транслитерации имени файла
def normalize(name: str) -> str:
    trans_name = name.translate(TRANS)
    return trans_name


# Словарь с категориями файлов и их расширениями
CATEGORIES = {"Audio": [".mp3", ".aiff", ".amr", ".ogg", ".wav"],
              "Documents": [".doc", ".docx", ".rtf", ".xlsx", ".pptx", ".txt", ".pdf"],
              "Images":[".jpeg", ".png", ".jpg", ".svg"],
              "Video":[".avi", ".mp4", ".mov", ".mkv",],
              "Archives":[".zip", ".gz", ".tar"]}

# Списки известных и неизвестных расширений файлов
known_extensions = []
unknown_extensions = []


# Функция для перемещения файла в соответствующую категорию
def move_file(file: Path, root_dir: Path, category: str) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    if new_name.exists():
       new_name = new_name.with_name(f"{new_name.stem}-{uuid.uuid4()}{file.suffix}")
    file.rename(new_name)
    

# Функция для определения категории файла
def get_category(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            if ext not in known_extensions:
                known_extensions.append(ext)
            return cat
    if ext not in unknown_extensions:
        unknown_extensions.append(ext)
    return "Other"


# Функция для сортировки файлов в папке
def sort_folder(path: Path) -> None:
    for item in path.glob("**/*"):
        if item.is_file():
            if str(item).find('Archives') == -1 and str(item).find('Video') == -1 and str(item).find('Audio') == -1 and str(item).find('Documents') == -1 and str(item).find('Images') == -1:
                cat = get_category(item)
                move_file(item, path, cat)

                
# Функция для удаления пустых папок
def delete_empty_dirs(path: Path) -> None:
    for item in path.glob("**/*"):
        if item.is_dir():
            delete_empty_dirs(item)
            if len(list(item.iterdir())) == 0:
                item.rmdir()

                
# Функция для извлечения архивов
def unpack_archives(path: Path) -> None:
    p = Path(path, "Archives")
    for item in p.glob("*"):
        if item.suffix == ".zip" or item.suffix == ".gz" or item.suffix == ".tar":  
            target_dir = p.joinpath(item.stem)
            if not target_dir.exists():
                target_dir.mkdir()
            shutil.unpack_archive(item, target_dir)
            item.unlink()

            
# Функция для списка файлов в папке
def list_files(path: Path) -> str:
    list_all = "\nAll found files have been sorted:\n"
    for item in path.glob("**/*"):
        if item.is_dir():
            list_all += f"\nfolder: {item}:\n"
            for files in item.glob("**/*"):
                if files.is_dir():
                    list_all += f"subfolder: {files.stem}:\n"
                if files.is_file():
                    list_all += f"{files.stem}{files.suffix}\n"
    return list_all


# Основная функция
def main(path_str: str = None) -> str:
    if path_str is None:
        path_str = sys.argv[1]
    try:
        path = Path(path_str)
    except IndexError:
        return "No path to folder"
    if not path.exists():
        return f"Folder with path '{path}' does not exist."
    
    sort_folder(path)
    delete_empty_dirs(path)
    unpack_archives(path)
    result = []
    result.append(list_files(path))
    result.append(f"\nFound known file extensions: {known_extensions}")
    result.append(f"\nFound unknown file extensions: {unknown_extensions}")
    result.append("\nFinish")
    return "\n".join(result)


if __name__ == "__main__":
    print(main())