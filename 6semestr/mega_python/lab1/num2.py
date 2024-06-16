from zipfile import ZipFile
import os


def human_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    index = 0
    for i in range(len(sizes)):
        if size / (1024**i) < 1:
            break
        index = i
    return f'{round(size / (1024 ** index))}{sizes[index]}'


with ZipFile('archive.zip') as zf:
    for name in zf.namelist():
        items = name.rstrip("/").split("/")
        mark = False
        for i in items:
            if "." in i:
                mark = True
        if not (mark):
            continue
        size = zf.getinfo(name).file_size
        dir_path = ""
        for i in range(len(items) - 1):
            dir_path += "  " + items[i]
        print(dir_path + "  " + items[-1] + '  ' + human_format(size))
