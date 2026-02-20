import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("❌ Directory not found!")
        return

    # File categories
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Programs": [".py", ".java", ".c", ".cpp"]
    }

    file_count = 0

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            for folder, extensions in categories.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved: {file} → {folder}")
                    file_count += 1
                    break

    print(f"\n✅ Total files organized: {file_count}")


if __name__ == "__main__":
    path = input("Enter directory path to organize: ")
    organize_files(path)