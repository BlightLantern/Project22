import tkinter as tk
from dir import Dir
from PIL import ImageTk

#button functionalities
funcObj = Dir('directory_Object')
class ButtonFunc():
    def __init__(self,frame) -> None:
        self.frame=frame
        pass
    def getInformation(self):
        funcObj.getPath()
        funcObj.getItems()
    def placeImage(self):
        try:
            self.label.destroy()
        except:
            pass
        image = funcObj.getImage()
        imageP = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.frame, image = imageP)
        self.label.photo = imageP
        self.label.pack()

    def openDirectory(self):        #Button command
        self.getInformation()
        self.placeImage()

    def Pindex(self):       #Button command
        funcObj.getPindex()
        self.placeImage()

    def Mindex(self):       #Button command
        funcObj.getMindex()
        self.placeImage()

    def destroy(self):
        funcObj.destroy()
        del self