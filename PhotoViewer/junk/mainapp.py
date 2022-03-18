import tkinter
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os


#choose directory funcionality:
class func:
    def __init__(self) -> None:
        pass

    index=0

    def Filename(self):   # Finds Path
        filename = filedialog.askdirectory(initialdir='C:\\', mustexist=True) #stores path
        if filename:
            self.path=filename+'/'

    def dir_files(self):    # Return files in Path, and path
        f_list=[]
        for f in os.listdir(self.path):
            if f.endswith(('.jpg','.jpeg','.png')):
                f_list.append(f)
        self.dir_list = f_list

    def place_image(self, i):       # To place image in label
        try:
            self.reset()
            image = Image.open(str(self.path)+str(self.dir_list[i]))
            resized_image= image.resize((900,600), Image.ANTIALIAS)
            imageP = ImageTk.PhotoImage(resized_image)
            self.label = tkinter.Label(frame, image = imageP)
            self.label.photo = imageP
            self.label.pack()
        except IndexError:
            pass

    def reset(self):
        if abs(self.index)>len(self.dir_list)-1:
            if self.index<0:
                self.index+=1
            elif self.index>0:
                self.index-=1
            i=1+'i'    # To invoke exception in place_image, cause dir_list[-1] will return pic, causing 2 pics
            pass
        else:
            try:
                self.label.destroy()
            except:
                pass

    def directory(self):    #  When opening a new directory
        self.index = 0
        self.Filename()
        self.dir_files()
        self.place_image(self.index)
        self.items = len(self.dir_list)

    def changeIndexM(self):   # Changing photo to the left
        #self.index = self.index-1
        try:
            self.index = self.index-1
            self.place_image(self.index)
        except:
            pass

    def changeIndexP(self):    # Changing photo to the right
        try:
            self.index = self.index+1
            self.place_image(self.index)
        except:
            pass


#initialize object:
obj = func()

# close app function
def close():
    app.destroy()

#initialize tk window:
app = tkinter.Tk()
app.geometry("1000x700")

#image frame:
frame = tkinter.Frame(app, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
# highlightbackground="blue", highlightthickness=2 //To put border to frame

#buttons
buttonEX= tkinter.Button(app, text='Exit',width=4, height=4, command=close)
buttonEX.pack(side='left')
buttonEX.place(anchor='nw')
button1 = tkinter.Button(app, text='open directory', command=obj.directory)
button1.pack(side='top')
button2 = tkinter.Button(app, text='>',width=10, height=10, command=obj.changeIndexP)
button2.pack(side='right', padx=15, pady=20)
button3 = tkinter.Button(app, text='<',width=10, height=10, command=obj.changeIndexM)
button3.pack(side='left', padx=15, pady=20)

app.mainloop()