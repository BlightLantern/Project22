import tkinter
import directory   #Local

print(directory)
print(tkinter)

class application:
    def __init__(self) -> None:
        #initialize app:
        app = tkinter.Tk()
        self.app = tkinter.Tk()
        self.app.geometry("1000x700")
        dir = directory.Dir()

        #image frame:
        self.frame = tkinter.Frame(app, width=600, height=400)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        #buttons
        self.buttonEX= tkinter.Button(app, text='Exit',width=4, height=4, command=self.close)
        self.buttonEX.pack(side='left')
        self.buttonEX.place(anchor='nw')
        self.button1 = tkinter.Button(app, text='open directory', command=dir)
        self.button1.pack(side='top')
        self.button2 = tkinter.Button(app, text='>',width=10, height=10, command=dir.changeIndexP)
        self.button2.pack(side='right', padx=15, pady=20)
        self.button3 = tkinter.Button(app, text='<',width=10, height=10, command=dir.changeIndexM)
        self.button3.pack(side='left', padx=15, pady=20)

        # To close app
    def close(self):
        self.app.destroy()


app = application()