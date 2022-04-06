from directories_handler import DirectoriesHandler
from PIL import Image, ImageTk
from tkinter import Label


#$ Can you find a better name for self.Label and self.Image? so I can know what does they represent without reading all the class?
class ImageHandler(DirectoriesHandler):
    def __init__(self) -> None:
        super().__init__(self)
        self.imageExtensions = ('.jpg','.jpeg','.png')

    def getCurrentImage(self):
        self.image = Image.open(str(self.path)+str(self.directoryFilesList[self.listIndex]))
    
    def resizeImage(self, width, height):
        modifiedImage = self.image.resize((width, height), Image.ANTIALIAS)
        self.image = modifiedImage
    
    def getResizedImage(self, width, height):
        self.getCurrentImage()
        self.resizeImage(width, height)

    def returnPhotoImage(self):
        return ImageTk.PhotoImage(self.image)

    def destroy(self):
        del self