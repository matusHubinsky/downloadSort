import os
import shutil


name = input("User")
## name = 'leviathan'

if (os.path.exists('/home/' + name + '/.config/dowloandSort/') == False):
    print('Creating ~/.config')
    os.makedirs('/home/' + name + '/.config/dowloandSort/', exist_ok = True)

print('Opening ~/.config/saved.txt.')

o = open('/home/' + name + '/.config/dowloandsSort/saved.txt', 'a+')
file_type = [int(file_type) for file_type in o.readlines()]
file_path = '/home/' + name + '/Downloads'
download_list = os.listdir(file_path)
extension = ''

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


print('Closing ~/.config/saved.txt')
o.close()
print('Done.') 
