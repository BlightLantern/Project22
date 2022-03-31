from tkinter import filedialog
import os

class DirectoriesHandler():
    def __init__(self, name) -> None:
        self.name = name
        self.listIndex = 0
        pass

    def choosePath(self):
        path = filedialog.askdirectory(initialdir='C:\\', mustexist=True) 
        if path:
            self.path=path+'/'

    def getFiles(self, extensions):
        self.directoryFilesList=[]
        for f in os.listdir(self.path):
            if f.lower().endswith(extensions):
                self.directoryFilesList.append(f)
        self.imageListLenght = len(self.directoryFilesList)

    def doNext(self):
        self.listIndex+=1
        if self.listIndex>self.imageListLenght-1:
            self.listIndex=0
    
    def doBack(self):
        self.listIndex-=1
        if self.listIndex<(-self.imageListLenght):
            self.listIndex=0

    def destroy(self):
        del self

    
    
    