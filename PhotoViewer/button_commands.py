from image_handler import ImageHandler
import tkinter as tk

imageObject = ImageHandler()
#$ You seperated the commands of the button in a seperate class, why did you do it? It is not wrong i just want to know the logic behind it
#$ Buttons belong to the UI, so you could actually have left this in main.py
#button functionalities
class ButtonCommands(tk.Canvas):
    def __init__(self, app, width, height):
        super().__init__(master=app, width=width, height=height)
        self.imageWidth, self.imageHeight = 900, 600
        self.isImageExistant = False

    def OpenDirectory_Button(self):        #Button command
        imageObject.listIndex=0
        imageObject.choosePath()
        imageObject.getFiles(imageObject.imageExtensions)
        if self.isImageExistant:
            self.delete()
        imageObject.getResizedImage(self.imageWidth, self.imageHeight)
        self.image = self.create_image((self.imageWidth, self.imageHeight), image = imageObject.returnPhotoImage(), anchor='nw')
        self.isImageExistant = True
        self.update()

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            self.delete()
            imageObject.getResizedImage(self.imageWidth, self.imageHeight)
            self.image = self.create_image(self.imageWidth, self.imageHeight, image = imageObject.returnPhotoImage())

        except:
            print('error')
            pass

    def Minus_Button(self):       #Button command
        try:
            imageObject.doBack()
            self.delete()
            imageObject.getResizedImage(self.imageWidth, self.imageHeight)
            self.image = self.create_image(self.imageWidth, self.imageHeight, image = imageObject.returnPhotoImage())

        except:
            pass

    def deleteImage(self):
        self.delete('all')
        self.isImageExistant = False

    def destroy(self):
        imageObject.destroy()
        del self
    

    penIsDown = False

    def savePosition(self, event):
        self.x, self.y = event.x, event.y

    def addLine(self, event):
        self.create_line((self.x, self.y, event.x, event.y))
        self.savePosition(event)

    def changePen(self):
        if self.penIsDown:
            self.penIsDown = False
            self.unbind("<Button-1>")
            self.unbind("<B1-Motion>")
        else:
            self.penIsdown = True
            self.bind("<Button-1>", self.savePosition)
            self.bind("<B1-Motion>", self.addLine)
