import tkinter as tk
from PIL import Image, ImageTk
from button_commands import *

app=tk.Tk()
app.geometry("1000x700")

#main container dimesions:
width = 900
height = 600

'''#image container:
frame = tk.Frame(app, width=width, height=height, background='blue')
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)'''

#main container
# canvas = buttonCommandsCanvasSet(app, width=width, height=height)
# canvas.pack()
# canvas.place(anchor='center', relx=0.5, rely=0.5)

#main container
canvas = ButtonCommands(app, width, height, 'grey')
canvas.imageWidth, canvas.imageHeight = width, height
canvas.pack()
canvas.place(anchor='center', relx=0.5, rely=0.5)

#to close app
def close():
    canvas.destroy()
    app.destroy()

#buttonsMain
buttonExitDimension = 4

buttonEX= tk.Button(app, text='Exit',width=buttonExitDimension, height=buttonExitDimension, command=close)
buttonEX.pack(side='left')
buttonEX.place(anchor='nw')

#buttonsImageSet
buttonDirectionDimension = 10

buttonDir = tk.Button(app, text='open directory', command=canvas.OpenDirectory_Button)
buttonDir.pack(side='top')
buttonRight = tk.Button(app, text='>',width=buttonDirectionDimension, height=buttonDirectionDimension, command=canvas.Plus_Button)
buttonRight.pack(side='right', padx=15, pady=20)
buttonLeft = tk.Button(app, text='<',width=buttonDirectionDimension, height=buttonDirectionDimension, command=canvas.Minus_Button)
buttonLeft.pack(side='left', padx=15, pady=20)

#buttonsCanvasSet
buttonToolDimensions = 30
icon = ImageTk.PhotoImage(image=Image.open('./other/pen.png').resize((buttonToolDimensions, buttonToolDimensions)))
buttonPen = tk.Button(app, image=icon, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.changePen)
buttonPen.pack(side='bottom')

if __name__=='__main__':
    app.mainloop()