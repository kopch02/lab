import os


def human_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    index = 0
    for i in range(len(sizes)):
        if size / (1024**i) < 1:
            break
        index = i
    return f'{round(size / (1024 ** index))}{sizes[index]}'


def get_files_sizes():
    a = {}
    os.chdir('C:\ycheba\lab')
    for i in os.listdir():
        size = 0
        if os.path.isdir(i):
            size += get_size(i)
            a[f'{i} {human_format(size)}'] = size
        if os.path.isfile(i):
            size = os.path.getsize(i)
            a[f'{i} {human_format(size)}'] = size

    return a


def get_size(path):
    size = 0
    os.chdir(f'{path}')
    for i in os.listdir():
        if os.path.isfile(i):
            size += os.path.getsize(i)
        if os.path.isdir(i):
            size += get_size(i)
    os.chdir(f'..')
    return size


res = get_files_sizes()
res = sorted(res, key=res.get, reverse=True)
for i in res[:10]:
    print(i)
