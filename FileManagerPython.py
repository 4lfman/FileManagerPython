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
            print (filename)

            sub_folder = time.ctime(os.path.getctime(src)) #Gets the time in seconds since 1970 and converts to string
            sub_folder = time.strptime(sub_folder) #Gets the time from the string
            sub_folder = time.strftime("%Y-%m", sub_folder) #Formats the folders with year and month of the file creation

            new_destination = folder_destination + "/" + sub_folder
            
            if not (os.path.isdir(new_destination)): #If the directory does not exist, create it
                os.mkdir(new_destination)

            os.rename(src, new_destination + "/" + filename) #Move the file/folder to the new directory

folder_to_track = "/Users/Alfred/Desktop/Folder1"
folder_destination = "/Users/Alfred/Desktop/Folder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True: #Keeps the program running
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop() #Closes the observer
observer.join() #Read more on https://stackoverflow.com/questions/44401653/watchdog-observer-method https://stackoverflow.com/questions/19138219/use-of-threading-thread-join
