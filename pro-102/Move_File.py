import sys
import time
import random
import os
import shutil

from watchdogs.observers import Observer
from watchdog.events import FileSystemEventHandlers


from_dir = "c:/users/Downloads"
to_dir = "c://users/DownloadedFiles"

class FileMovementHandler(FileSystemEventHandler):

    list_of_files = os.listdir(from_dir)
    print(list_of_files)
    for file_name in list_of_files:
        name, extension = os.path.split_text(file_name)
        print(list_of_files)
        if extension == '':
                continue
        if extension in ['.txt', '.doc', '.docx', '.pdf']:
            path_one = from_dir + '/' + file_name
            path_two = to_dir + '/' + "image_files"
            path_three = to_dir + '/' + "image_files" + file_name
            if os.path.exists(path_two):
                shutil.move(path_one, path_three)
            else:
                os.mk_dirs(path_two)
                shutil.move(path_one, path_three)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
     while True:
          time.sleep(2)
          print("running..")
except KeyboardInterrupt:
     print("stopped!")
     observer.stop()