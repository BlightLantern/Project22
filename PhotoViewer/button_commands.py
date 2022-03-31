from logging import exception
from unittest import expectedFailure
from image_handler import ImageHandler

imageObject = ImageHandler()
#$ You seperated the commands of the button in a seperate class, why did you do it? It is not wrong i just want to know the logic behind it
#$ Buttons belong to the UI, so you could actually have left this in main.py
#button functionalities
class ButtonCommands():
    def __init__(self,frame) -> None:
        self.frame=frame
        self.imageWidth, self.imageHeight = 900, 600
        pass

    def OpenDirectory_Button(self):        #Button command
        imageObject.listIndex=0
        imageObject.choosePath()
        imageObject.getFiles(imageObject.imageExtensions)
        if imageObject.imagecontainer:
            imageObject.deleteCurrentImage()
        imageObject.getResizedImage(self.imageWidth, self.imageHeight)
        imageObject.displayImage(self.frame)

    def Plus_Button(self):       #Button command
        try:
            imageObject.doNext()
            imageObject.deleteCurrentImage()
            imageObject.getResizedImage(self.imageWidth, self.imageHeight)
            imageObject.displayImage(self.frame)
        except:
            print('error')
            pass

    def Minus_Button(self):       #Button command
    #$ Ask me to give you the exceptions remark, I saw that u use them extensively
        try:
            imageObject.doBack()
            imageObject.deleteCurrentImage()
            imageObject.getResizedImage(self.imageWidth, self.imageHeight)
            imageObject.displayImage(self.frame)
        except:
            pass

    def destroy(self):
        imageObject.destroy()
        del self