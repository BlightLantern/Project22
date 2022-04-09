from tkinter.colorchooser import askcolor
from image_handler import ImageHandler
import tkinter as tk
from tkinter import PhotoImage

imageObject = ImageHandler()

class ButtonCommands(tk.Canvas):
    def __init__(self, app, width, height, bg):
        super().__init__(master=app, width=width, height=height, bg=bg)
        self.imageWidth, self.imageHeight = width, height
        self.isImageExistant = False
        self.eventSequence = ('<Button-1>', "<B1-Motion>", "<ButtonRelease-1>")
        self.color = 'black'            #defailt drawing color
        self.shapeIds = []          #Store shape ids to delete them later

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
        self.tag_lower(self.image)

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            self.delete()
            self.placeImage()
            self.tag_lower(self.image)
        except: pass

    def Minus_Button(self):       #Button command
        try: 
            imageObject.doBack()
            self.delete()
            self.placeImage()
            self.tag_lower(self.image)
        except: pass

    def deleteImage(self):
        self.delete(self.image)
        self.isImageExistant = False

    def destroy(self):
        imageObject.destroy()
        del self
    

    #drawing functionalities

    def savePosition(self, event):
        self.x, self.y = event.x, event.y

    def pointer(self):
        for j in self.eventSequence:
            self.unbind(j)

            
    #pen
    def addLine(self, event):
        self.create_line((self.x, self.y, event.x, event.y), fill=self.color)
        self.savePosition(event)

    def penDown(self):
        self.pointer()
        self.bind("<Button-1>", self.savePosition)
        self.bind("<B1-Motion>", self.addLine)
    

    #rectangle
    def addRectangle(self, event):
        if self.x and self.y:
            self.shapeIds.append(self.create_rectangle((self.x, self.y, event.x, event.y), fill=self.color))

    def rectangleDown(self):
        self.pointer()
        self.x , self.y =  None, None
        self.bind('<Button-1>', self.savePosition)
        self.bind('<ButtonRelease-1>', self.addRectangle)

    #circle
    def addCircle(self, event):
        self.shapeIds.append(self.create_oval((self.x, self.y, event.x, event.y), fill = self.color))

    def circleDown(self):
        self.pointer()
        self.x, self.y = None, None
        self.bind("<Button-1>", self.savePosition)
        self.bind("<ButtonRelease-1>", self.addCircle)

    #color
    def askcolor(self):
        tuple, self.color = askcolor()

    #undo
    def undo(self):
        try:
            self.delete(self.shapeIds[-1])
            self.shapeIds.pop()
        except IndexError:
            pass

    #clear
    def clear(self):
        self.delete('all')
        try: 
            self.image = self.create_image(0, 0, image = imageObject.photoImage, anchor='nw')
        except:
            pass


