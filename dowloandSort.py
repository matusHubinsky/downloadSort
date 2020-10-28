import os
import shutil


if (not os.path.exists('home/leviathan/.config/dowloandSort/')):
    os.makedirs('home/leviathan/.config/dowloandSort/', exist_ok = True)
    print('Creating ~/.config/dowloandsort')

if (not os.path.exists('/home/leviathan/.config/dowloandSort/saved.txt')):
    o = open('/home/leviathan/.config/dowloandSort/saved.txt', 'x')
    print('Creating ~/.config/downloandSort/saved.txt')

print('Opening ~/.config/dowloandSort/saved.txt.')

o = open('home/leviathan/.config/dowloandSort/saved.txt', 'a+')
file_type = [int(file_type) for file_type in o.readlines()]
file_path = '/home/leviathan/Downloads'
download_list = os.listdir(file_path)
extension = ''

print('Opening ~/Dowloand')
print('Starting file transfer...')

for file in download_list:
    divided = file.split('.')

    if (len(divided) == 1):
        if (divided not in file_type):
            print("Don't sent: " + file)
    else:
        extension = divided[len(divided)-1]

        if (extension not in download_list): 
            os.makedirs(file_path + '/' + extension, exist_ok = True) 
            if (extension not in file_type): 
                file_type.append(str(extension))
                o.write(str(extension) + ' ') 
        else:
            new = file_path + '/' + extension
            shutil.move(file_path + '/' + str(file), new)
            print('Sent:', file)

print('Closing ~/.config/downloandSort/saved.txt')
print('Done.')
o.close()

## place this file to /home/user_name/.dowloandsort/
