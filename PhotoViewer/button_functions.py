import tkinter as tk
from image_handler import ImageHandler
from PIL import ImageTk

imageObject = ImageHandler()

#button functionalities
class ButtonFunc():
    def __init__(self,frame) -> None:
        self.frame=frame
        pass

    def placeImage(self):
        try:
            self.label.destroy()
        except:
            pass
        imageObject.doImage()
        imageP = ImageTk.PhotoImage(imageObject.image)
        self.label = tk.Label(self.frame, image = imageP)
        self.label.photo = imageP
        self.label.pack()

    def OpenDirectory_Button(self):        #Button command
        imageObject.index=0
        imageObject.getDir()
        self.placeImage()

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            self.placeImage()
        except:
            pass

    def Minus_Button(self):       #Button command
        try:
            imageObject.doBack()
            self.placeImage()
        except:
            pass

    def destroy(self):
        imageObject.destroy()
        del self