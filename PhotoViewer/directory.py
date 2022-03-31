from tkinter import filedialog
import os

#$ The name of the file does not represent the name of the class, so If i were to search for Dir I would have to open every file
#$ Naming consistency and long descriptive names: Dir can be renamed for something like DirectoriesHandler?
class Dir():
    def __init__(self, name) -> None:
        self.name = name
        self.index = 0
        pass

    #$ You're actually choosing a pass here not getting one right?
    def getPath(self):
        path = filedialog.askdirectory(initialdir='C:\\', mustexist=True) 
        if path:
            self.path=path+'/'

    #$ you are actually getting files or image files, more expressive right?
    def getItems(self):
        #$ so you are filling an array from a tuple, then copying the array to another array?
        #$ the list of extensions is supported by your code, why do you need to do this?
        f_list=[]
        for f in os.listdir(self.path):
            if f.endswith(('.jpg','.jpeg','.png')):
                f_list.append(f)
        self.dir_list = f_list
        self.items = len(self.dir_list)

    #$ Any better naming suggestion? Youll find that this function is not needed as you are naming it
    def getDir(self):
        self.getPath()
        self.getItems()

    #$ Perfectly understood the seperation of concerns here bravo !
    def doNext(self):
        self.index+=1
        if self.index>self.items-1:
            self.index=0
    
    def doBack(self):
        self.index-=1
        if self.index<(-self.items):
            self.index=0

    def destroy(self):
        del self

    
    
    