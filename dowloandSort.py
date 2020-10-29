import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "/home/leviathan/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if (event.is_directory):
            if (not os.path.exists('/home/leviathan/.config/dowloandSort')):
                os.makedirs('/home/leviathan/.config/dowloandSort', exist_ok=True)
                print('Creating ~/.config/dowloandsort')

            if (not os.path.exists('/home/leviathan/.config/dowloandSort/saved.txt')):
                open('/home/leviathan/.config/dowloandSort/saved.txt', 'x')
                print('Creating ~/.config/downloandSort/saved.txt')

            if (not os.path.exists('/home/leviathan/.config/autostart/python.desktop')):
                open('/home/leviathan/.config/autostart/python.desktop', 'x')
                print('Creating ~/.config/autostart/python.desktop')
            
            print('Opening ~/.config/dowloandSort/saved.txt.')

            o = open('/home/leviathan/.config/dowloandSort/saved.txt', 'a+')
            file_type = [int(file_type) for file_type in o.readlines()]
            file_path = '/home/leviathan/Downloads'
            download_list = os.listdir(file_path)
            extension = ''
            dontSent = []
            Sent = []

            print('Opening ~/Dowloand')
            print('Starting file transfer...')

            for file in download_list:
                divided = file.split('.')

                if (len(divided) == 1):
                    if (divided not in file_type):
                        dontSent.append(file)
                else:
                    extension = divided[len(divided) - 1]

                    if (extension not in download_list):
                        os.makedirs(file_path + '/' + extension, exist_ok=True)
                        if (extension not in file_type):
                            file_type.append(str(extension))
                            o.write(str(extension) + ' ')
                            Sent.append(file)
                    else:
                        new = file_path + '/' + extension
                        shutil.move(file_path + '/' + str(file), new)
                        Sent.append(file)

            for element in dontSent:
                print("Don't sent:", element)

            for element in Sent:
                print("Sent:", element)

            print('Closing ~/.config/downloandSort/saved.txt')
            print('Done.')
            o.close()

if __name__ == '__main__':
    w = Watcher()
    w.run()

