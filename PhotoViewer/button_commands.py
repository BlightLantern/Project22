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
        self.isRectangleDown = False
        self.isCircleDown = False
        self.pens=(self.isPenDown, self.isRectangleDown, self.isCircleDown)

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
    eventSequence = ('<Button-1>', "<B1-Motion>", "<ButtonRelease-1>")

    def savePosition(self, event):
        self.x, self.y = event.x, event.y

    def unbinding(self):
        for i in self.pens:
            i = False
        for j in self.eventSequence:
            self.unbind(j)
            
            
    #pen
    def addLine(self, event):
        self.create_line((self.x, self.y, event.x, event.y))
        self.savePosition(event)

    def penDown(self):
        self.unbinding()
        self.isPenDown = True
        self.bind("<Button-1>", self.savePosition)
        self.bind("<B1-Motion>", self.addLine)
    

    #rectangle
    def addRectangle(self, event):
        if self.x and self.y:
            self.create_rectangle((self.x, self.y, event.x, event.y), fill='red')

    def planRectangle(self):
        self.x , self.y =  None, None
        self.unbinding()
        self.isRectangleDown = True
        self.bind('<Button-1>', self.savePosition)
        self.bind('<ButtonRelease-1>', self.addRectangle)



