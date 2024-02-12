import os
import time
import datetime

PATH = "C:\\Users\\daszyma\\Downloads"
files = os.listdir(PATH)


def remove_files_by_extension(files):

    extensions = ('.jnlp', '.zip')

    for file in files:
        file_extension = os.path.splitext(file)
        for extension in extensions:
            if file_extension[1] == extension:
                os.remove(os.path.join(PATH, file))


def pdf_to_folder(files):

    folder_name = "\\PDF_folder"
    folder_path = PATH + folder_name

    if not os.path.exists(folder_name):
        os.mkdir(folder_path)
        time.sleep(1)
    else:
        for file in files:
            file_extension = os.path.splitext(file)
            if file_extension[1] == ".pdf":
                os.rename(os.path.join(PATH, file), os.path.join(folder_path, file))


# files = os.listdir(PATH)
# for file in files:
#     time_files = datetime.datetime.fromtimestamp(os.path.getatime(os.path.join(PATH, file)))
#     print(time_files)

if __name__ == "__main__":
    remove_files_by_extension(files)
    pdf_to_folder(files)
