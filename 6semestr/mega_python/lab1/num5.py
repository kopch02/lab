from zipfile import ZipFile
import os
import json
import shutil

with ZipFile('num5_test.zip') as myzip:
    myzip.extractall('./zip')
    os.chdir(f'zip')
    count = 0
    for currentdir, dirs, files in os.walk('.'):
        size = 0
        for i in files:
            try:
                with open(os.path.join(currentdir, i)) as json_file:
                    f = json.load(json_file)
                    if f["city"] == "moscow":
                        count += 1
            except:
                print("был найден другой файл")
    print(f"{count = }")
os.chdir('..')
shutil.rmtree("zip")
