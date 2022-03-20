from directory import Dir
from PIL import Image

class ImageHandler(Dir):
    def __init__(self) -> None:
        super().__init__(self)
        self.index = 0

    def getImage(self):
        self.image = Image.open(str(self.path)+str(self.dir_list[self.index]))
    
    def doImageModification(self):
        modifiedImage = self.image.resize((900,600), Image.ANTIALIAS)
        self.image = modifiedImage
    
    def doImage(self):
        self.getImage()
        self.doImageModification()

    def doNext(self):
        self.index+=1
        if self.index>self.items-1:
            self.index=0
    
    def doBack(self):
        self.index-=1
        if self.index<(-self.items):
            self.index=0

    def destroy(self):
        del self