import os
import shutil
import time


def new_name(file_name, file_ext, file_path, i):
    same_name = file_path + '/' + file_ext + '/' + file_name + file_ext

    if (os.path.exists(same_name)):
        if ((ord(file_name[len(file_name) - 1]) >= 48) and (ord(file_name[len(file_name) - 1]) <= 57)):
            a = int(file_name[len(file_name) - 1]) + 1
            return new_name(file_name[:len(file_name) - 1] + str(a), file_ext, file_path, i + 1)
        else:
            return new_name(file_name + str(i), file_ext, file_path, i + 1)
    return file_name + file_ext


print('Checking folders...')

if (not os.path.exists('/home/leviathan/.config/dowloandSort')):
    os.makedirs('/home/leviathan/.config/dowloandSort', exist_ok=True)
    print('Creating ~/.config/dowloandsort')

if (not os.path.exists('/home/leviathan/.config/dowloandSort/saved.txt')):
    open('/home/leviathan/.config/dowloandSort/saved.txt', 'x')
    print('Creating ~/.config/downloandSort/saved.txt')

if (not os.path.exists('/home/leviathan/.config/autostart/python.desktop')):
    open('/home/leviathan/.config/autostart/python.desktop', 'x')
    print('Creating ~/.config/autostart/python.desktop')

o = open('/home/leviathan/.config/dowloandSort/saved.txt', 'a+')
file_types = [int(file_types) for file_types in o.readlines()]
file_path = '/home/leviathan/Downloads'

while (True):
    for file in os.listdir(file_path):
        file_name, file_ext = os.path.splitext(file)

        if (file_ext):
            if (not (file_ext in file_types)):
                os.makedirs(file_path + '/' + file_ext, exist_ok=True)
                o.write(str(file_ext))

            new = new_name(file_name, file_ext, file_path, 1)
            os.rename(file, new)
            print(new)
            shutil.move(file_path + '/' + file, file_path + '/' + file_ext + '/' + new)
            print("Sent:", file)

    print('I am waiting')
    time.sleep(10)
