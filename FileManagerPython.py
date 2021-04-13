from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            HandleFile(filename)

def HandleFile(filename):

    #The filetypes
    #region
    def folder():
        print(filename + ": Was a folder")
        return 'Folder'
    
    def picture():
        print(filename + ": Was a picture")
        return 'Picture'

    def txt():
        print(filename + ":Was .txt")
        return 'txt'

    def zip():
        print(filename + ": Was a zip file")
        return 'zip'

    def lnk():
        print(filname + ': Was a shortcut(.lnk)')
        return 'Shortcut'

    def app():
        print(filename + ': Was an app')
        return 'App'

    def notAvalible():
        print("{} filetype is not avalible for now.".format(extention))
        return 'unavalible'
    
    #endregion

    src = folder_to_track + "/" + filename
    
    extention = os.path.splitext(filename)[1]
    if extention in ['.png', '.jpeg', '.jpg', '.gif']: #Lumps all picture formats into one method
        extention = 'picture'
    elif os.path.isdir(src): #Checks if the input is a folder
        extention = 'Folder'

    dict = {
        'Folder' : folder,
        'picture' : picture,
        '.txt' : txt,
        '.log' : txt,
        '.zip' : zip,
        '.lnk' : lnk,
        '.exe' : app
        }
    filetype = dict.get(extention, notAvalible)() #Assigns the return of the method from the dict to 'filetype'

    time_folder = time.ctime(os.path.getctime(src)) #Gets the time in seconds since 1970 and converts to string
    time_folder = time.strptime(time_folder) #Gets the time from the string
    time_folder = time.strftime("%Y-%m", time_folder) #Formats the folders with year and month of the file creation

    new_destination = (folder_destination + '/' + filetype + '/' + time_folder)

    if filetype != None:
        if not (os.path.isdir(new_destination)): #If the directory does not exist, create it
            os.makedirs(new_destination)
        os.rename(src, (new_destination + '/' + filename)) #Move the file/folder to the new directory

folder_to_track = "/Users/Alfred/Desktop/AutoSort"
folder_destination = "/Users/Alfred/Desktop/SortByFileType"
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
