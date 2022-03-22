import tkinter as tk
from image_handler import ImageHandler
from PIL import ImageTk

imageObject = ImageHandler()

#button functionalities
class ButtonFunc():
    def __init__(self,frame) -> None:
        self.frame=frame
        pass

    def OpenDirectory_Button(self):        #Button command
        imageObject.index=0
        imageObject.getDir()
        imageObject.doImage()
        imageObject.displayImage(self.frame)

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            imageObject.deleteImage()
            imageObject.displayImage(self.frame)
        except:
            pass

    def Minus_Button(self):       #Button command
        try:
            imageObject.doBack()
            imageObject.deleteImage()
            imageObject.displayImage(self.frame)
        except:
            pass

    def destroy(self):
        imageObject.destroy()
        del self