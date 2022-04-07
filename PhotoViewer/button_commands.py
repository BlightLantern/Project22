from image_handler import ImageHandler
import tkinter as tk
from tkinter import PhotoImage

imageObject = ImageHandler()

class ButtonCommands(tk.Canvas):
    def __init__(self, app, width, height, bg):
        super().__init__(master=app, width=width, height=height, bg=bg)
        self.imageWidth, self.imageHeight = 900, 600
        self.isImageExistant = False
        self.isPenDown = False

    def placeImage(self):
        imageObject.getResizedImage(self.imageWidth, self.imageHeight)
        imageObject.getPhotoImage()
        self.image = self.create_image(0, 0, image = imageObject.photoImage, anchor='nw')
        self.isImageExistant = True

    #image functionalities
    def OpenDirectory_Button(self):        #Button command
        imageObject.listIndex=0
        imageObject.choosePath()
        imageObject.getFiles(imageObject.imageExtensions)
        if self.isImageExistant:
            self.delete()
        self.placeImage()

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            self.delete()
            self.placeImage()
        except: pass

    def Minus_Button(self):       #Button command
        try: 
            imageObject.doBack()
            self.delete()
            self.placeImage()
        except: pass

    def deleteImage(self):
        self.delete('all')
        self.isImageExistant = False

    def destroy(self):
        imageObject.destroy()
        del self
    

    #drawing functionalities

    def savePosition(self, event):
        self.x, self.y = event.x, event.y

    def addLine(self, event):
        self.create_line((self.x, self.y, event.x, event.y))
        self.savePosition(event)

    def changePen(self):            #Button Command
        if self.isPenDown:
            self.isPenDown = False
            self.unbind("<Button-1>")
            self.unbind("<B1-Motion>")
        else:
            self.isPenDown = True
            self.bind("<Button-1>", self.savePosition)
            self.bind("<B1-Motion>", self.addLine)
