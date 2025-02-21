import os
import shutil

TARGET_FOLDER = "C:/Users/hasan/Downloads"

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Others": []
}


def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"


def organize_files():
    if not os.path.exists(TARGET_FOLDER):
        print(f"Error: Directory '{TARGET_FOLDER}' does not exist.")
        return

    files_moved = []
    for filename in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        category = get_category(file_extension)
        category_folder = os.path.join(TARGET_FOLDER, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        new_path = os.path.join(category_folder, filename)
        shutil.move(file_path, new_path)
        files_moved.append((filename, category))

    print(f" Organized {len(files_moved)} files successfully!")
    if files_moved:
        print("\n Moved Files:")
        for file, category in files_moved:
            print(f"  - {file} → {category}/")


if __name__ == "__main__":
    organize_files()
