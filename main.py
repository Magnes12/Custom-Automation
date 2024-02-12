import os 

PATH = 'C:\\Users\\daszyma\\Downloads'

files = os.listdir(PATH)

for file in files:
    extension = os.path.splitext(file)
    if extension[1] == '.jnlp':
        os.remove(os.path.join(PATH, file))
