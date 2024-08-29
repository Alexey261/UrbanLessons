import os
import time

start_dir = os.getcwd()
dirs = ['f_dir', 's_dir', 't_dir']

for i in dirs:
    if not os.path.exists(start_dir+'\\'+i):
        os.mkdir(i)
        os.chdir(i)
        with open(i.replace('dir','')+'file.txt', 'w') as f:
            pass

os.chdir(start_dir+'\\'+dirs[0])

for root, drs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.stat(filepath).st_size
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')



os.chdir(start_dir)

d = start_dir
for j in dirs:
    d += '\\' + j
    if os.path.exists(d):
        os.chdir(d)
        fname = j.replace('dir','')+'file.txt'
        if os.path.isfile(fname):
            os.remove(fname)

for i in range(len(dirs)):
    d = os.getcwd()
    os.chdir('..')
    os.rmdir(d)



