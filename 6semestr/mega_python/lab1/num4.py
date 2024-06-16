import datetime
import shutil
import os
from zipfile import ZipFile


def make_reserve_arc(source, dest):
    os.chdir(dest)
    date = str(datetime.datetime.now()).replace(" ", "_")
    date = date.replace(":", ".")
    with ZipFile('archive_' + date + ".zip", 'w') as myzip:
        os.chdir(source)
        for currentdir, dirs, files in os.walk('.'):
            for file in files:
                myzip.write(os.path.join(currentdir, file))


make_reserve_arc("C:\ycheba\lab\\6semestr\mega_python", "C:\Games")
