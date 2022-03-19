import tkinter as tk
from buttonfunc import ButtonFunc

app=tk.Tk()
app.geometry("1000x700")

#image frame:
frame = tk.Frame(app, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#button functionality object
Buttonf = ButtonFunc(frame)

#to close app
def close():
    Buttonf.destroy()
    app.destroy()

#buttons
buttonEX= tk.Button(app, text='Exit',width=4, height=4, command=close)
buttonEX.pack(side='left')
buttonEX.place(anchor='nw')
button1 = tk.Button(app, text='open directory', command=Buttonf.openDirectory)
button1.pack(side='top')
button2 = tk.Button(app, text='>',width=10, height=10, command=Buttonf.Pindex)
button2.pack(side='right', padx=15, pady=20)
button3 = tk.Button(app, text='<',width=10, height=10, command=Buttonf.Mindex)
button3.pack(side='left', padx=15, pady=20)

app.mainloop()