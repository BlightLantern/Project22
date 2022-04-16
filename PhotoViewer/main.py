import tkinter as tk
from PIL import Image, ImageTk
from button_commands import *

app=tk.Tk()
app.geometry("1000x700")

#main container dimesions:
width = 900
height = 600

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


#buttons drawing
toolsContainer = tk.Frame(app)
toolsContainer.pack(side='bottom')

buttonToolDimensions = 30

iconPointer = ImageTk.PhotoImage(image=Image.open('./other/pointer.png').resize((buttonToolDimensions, buttonToolDimensions)))
buttonPointer = tk.Button(toolsContainer, image=iconPointer, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.pointer)
buttonPointer.pack(side='right', padx=5, pady=5)

iconPen = ImageTk.PhotoImage(image=Image.open('./other/pen.png').resize((buttonToolDimensions, buttonToolDimensions)))
buttonPen = tk.Button(toolsContainer, image=iconPen, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.penDown)
buttonPen.pack(side='right', padx=5, pady=5)

iconRectangle = ImageTk.PhotoImage(image=Image.open('./other/rectangle.png').resize((buttonToolDimensions, buttonToolDimensions)))
buttonRectangle = tk.Button(toolsContainer, image=iconRectangle, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.rectangleDown)
buttonRectangle.pack(side='right', padx=5, pady=5)

iconCircle = ImageTk.PhotoImage(image=Image.open('./other/circle.jpg').resize((buttonToolDimensions, buttonToolDimensions)))
buttonCircle = tk.Button(toolsContainer, image=iconCircle, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.circleDown)
buttonCircle.pack(side='right', padx=5, pady=5)

iconColor = ImageTk.PhotoImage(image=Image.open('./other/colors.jpg').resize((buttonToolDimensions, buttonToolDimensions)))
buttonColor=tk.Button(toolsContainer, image=iconColor, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.askcolor)
buttonColor.pack(side='right', padx=5, pady=5)

iconUndo = ImageTk.PhotoImage(image=Image.open('./other/undo.jpg').resize((buttonToolDimensions, buttonToolDimensions)))
buttonUndo = tk.Button(toolsContainer, image=iconUndo, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.undo)
buttonUndo.pack(side='right', padx=5, pady=5)

iconClear = ImageTk.PhotoImage(image=Image.open('./other/clear.png').resize((buttonToolDimensions, buttonToolDimensions)))
buttonClear = tk.Button(toolsContainer, image=iconClear, width=buttonToolDimensions, height=buttonToolDimensions, command=canvas.clear)
buttonClear.pack(side='right', padx=5, pady=5)

if __name__=='__main__':
    app.mainloop()