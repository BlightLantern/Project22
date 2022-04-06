from tkinter import *

app = Tk()

canvas = Canvas(app, width=500, height=500, bg='grey')
canvas.pack()


img = PhotoImage(file="../PhotoViewer/other/pen.png")
print(img)
canvas.create_image(200,200, anchor=NW, image=img)

app.mainloop()