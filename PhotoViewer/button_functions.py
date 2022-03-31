import tkinter as tk
from image_handler import ImageHandler
from PIL import ImageTk

imageObject = ImageHandler()
#$ You seperated the commands of the button in a seperate class, why did you do it? It is not wrong i just want to know the logic behind it
#$ Buttons belong to the UI, so you could actually have left this in main.py
#button functionalities
#$ Naming, Since these are commands, I would opt for ButtonCommands
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
    #$ Ask me to give you the exceptions remark, I saw that u use them extensively
        try:
            imageObject.doBack()
            imageObject.deleteImage()
            imageObject.displayImage(self.frame)
        except:
            pass

    def destroy(self):
        imageObject.destroy()
        del self