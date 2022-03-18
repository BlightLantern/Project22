import tkinter
from directory import Dir   #Local


class application:
    def __init__(self):
        #initialize app:
        self.app = tkinter.Tk()
        self.app.geometry("1000x700")

        #image frame:
        self.frame = tkinter.Frame(self.app, width=600, height=400)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        #buttons
        self.buttonEX= tkinter.Button(self.app, text='Exit',width=4, height=4, command=self.close)
        self.buttonEX.pack(side='left')
        self.buttonEX.place(anchor='nw')
        self.button1 = tkinter.Button(self.app, text='open directory', command=Dir)
        self.button1.pack(side='top')
        self.button2 = tkinter.Button(self.app, text='>',width=10, height=10, command=Dir.changeIndexP)
        self.button2.pack(side='right', padx=15, pady=20)
        self.button3 = tkinter.Button(self.app, text='<',width=10, height=10, command=Dir.changeIndexM)
        self.button3.pack(side='left', padx=15, pady=20)

        #launching app
        self.app.mainloop()

        # To close app
    def close(self):
        self.app.destroy()

application()