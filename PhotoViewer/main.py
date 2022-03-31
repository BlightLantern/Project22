import tkinter as tk
from button_commands import ButtonCommands

app=tk.Tk()
app.geometry("1000x700")

#image frame:
frame = tk.Frame(app, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#button functionality object
Buttons = ButtonCommands(frame)

#to close app
def close():
    Buttons.destroy()
    app.destroy()

#buttons
buttonDirectionDimension = 10
buttonExitDimension = 4

buttonEX= tk.Button(app, text='Exit',width=buttonExitDimension, height=buttonExitDimension, command=close)
buttonEX.pack(side='left')
buttonEX.place(anchor='nw')
buttonDir = tk.Button(app, text='open directory', command=Buttons.OpenDirectory_Button)
buttonDir.pack(side='top')
buttonRight = tk.Button(app, text='>',width=buttonDirectionDimension, height=buttonDirectionDimension, command=Buttons.Plus_Button)
buttonRight.pack(side='right', padx=15, pady=20)
buttonLeft = tk.Button(app, text='<',width=buttonDirectionDimension, height=buttonDirectionDimension, command=Buttons.Minus_Button)
buttonLeft.pack(side='left', padx=15, pady=20)

app.mainloop()