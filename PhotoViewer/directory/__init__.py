from tkinter import filedialog, Label
from PIL import ImageTk, Image
import os
from tkinterApp import application   # Main app

class Dir:
    def __init__(self) -> None:
        # Getting and Storing path
        filename = filedialog.askdirectory(initialdir='C:\\', mustexist=True) 
        if filename:
            self.path=filename+'/'

        # Getting and storing files in Path
        f_list=[]
        for f in os.listdir(self.path):
            if f.endswith(('.jpg','.jpeg','.png')):
                f_list.append(f)
        self.dir_list = f_list

        # Index of image list, set to 0 by default
        self.index=0

        # Number of files in path
        self.items = len(self.dir_list)

    def placeImage(self):
        image = Image.open(str(self.path)+str(self.dir_list[self.index]))
        resized_image= image.resize((900,600), Image.ANTIALIAS)
        imageP = ImageTk.PhotoImage(resized_image)
        application.label = Label(application.frame, image = imageP)
        application.label.photo = imageP
        application.label.pack()

    def changeIndexP(self):
        self.index+=1
        if self.index>self.items:
            self.index=0
        self.placeImage(self.index)

    def changeIndexM(self):
        if self.index<(-self.items):
            self.index=0
        self.index-=1
        self.placeImage(self.index)