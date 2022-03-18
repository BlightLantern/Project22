from tkinter import filedialog, Label
from PIL import ImageTk, Image
import os

class Dir:
    def __init__(self):
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

        # Place initial image
        self.placeImage()

        print(self.path+self.dir_list[self.index])

    def placeImage(self):
        import tkinterApp   # Main app
        image = Image.open(str(self.path)+str(self.dir_list[self.index]))
        resized_image= image.resize((900,600), Image.ANTIALIAS)
        imageP = ImageTk.PhotoImage(resized_image)
        tkinterApp.application.label = Label(tkinterApp.application.frame, image = imageP)
        tkinterApp.application.label.photo = imageP
        tkinterApp.application.label.pack()

    def changeIndexP(self):
        self.index+=1
        if self.index>self.items:
            self.index=0
        self.placeImage()

    def changeIndexM(self):
        if self.index<(-self.items):
            self.index=0
        self.index-=1
        self.placeImage()