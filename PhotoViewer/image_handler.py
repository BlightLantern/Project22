from directory import Dir
from PIL import Image, ImageTk
from tkinter import Label

class ImageHandler(Dir):
    def __init__(self) -> None:
        super().__init__(self)
        self.img = True

    def getImage(self):
        self.image = Image.open(str(self.path)+str(self.dir_list[self.index]))
        self.img = True
    
    def doImageModification(self):
        modifiedImage = self.image.resize((900,600), Image.ANTIALIAS)
        self.image = modifiedImage
    
    def doImage(self):
        self.getImage()
        self.doImageModification()

    def displayImage(self, frame):
        self.deleteImage()
        if not self.img:
            self.doImage()
        imageP = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image = imageP)
        self.label.photo = imageP
        self.label.pack()

    def deleteImage(self):
        try:
            self.label.destroy()
            self.img = False
        except:
            pass

    def destroy(self):
        del self