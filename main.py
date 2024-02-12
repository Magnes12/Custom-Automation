import os

PATH = 'C:\\Users\\daszyma\\Downloads'


def remove_files_by_extension(PATH):

    files = os.listdir(PATH)
    extensions = ('.jnlp', '.zip')

    for file in files:
        file_extension = os.path.splitext(file)
        for extension in extensions:
            if file_extension[1] == extension:
                os.remove(os.path.join(PATH, file))


if __name__ == "__main__":
    remove_files_by_extension(PATH)
