from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename

            sub_folder = time.ctime(os.path.getctime(src))
            sub_folder = time.strptime(sub_folder)
            sub_folder = time.strftime("%Y-%m", sub_folder)

            new_destination = folder_destination + "/" + sub_folder
            
            if not (os.path.isdir(new_destination)):
                os.mkdir(new_destination)

            os.rename(src, new_destination + "/" + filename)

folder_to_track = "/Users/Alfred/Desktop/Folder1"
folder_destination = "/Users/Alfred/Desktop/Folder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
