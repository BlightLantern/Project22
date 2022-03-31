from directory import Dir
from PIL import Image, ImageTk
from tkinter import Label

#$ Use long descriptive names, self.img can actually be -> isImageLoaded
#$ Can you find a better name for self.Label and self.Image? so I can know what does they represent without reading all the class?
#$ Image Handler is a good name !
class ImageHandler(Dir):
    def __init__(self) -> None:
        super().__init__(self)
        self.img = True

    #$ getCurrentImage?
    def getImage(self):
        self.image = Image.open(str(self.path)+str(self.dir_list[self.index]))
        self.img = True
    
    #$ Your actually resizing the image, why not call it resizeImage as its more expressive?
    def doImageModification(self):
        #$ Separation of concerns: isn't the resize thing a UI concern?
        #$ if you use this handler for another app that have other dimensions, what do you do?
        modifiedImage = self.image.resize((900,600), Image.ANTIALIAS)
        self.image = modifiedImage
    
    #$ Any better naming suggestion?
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