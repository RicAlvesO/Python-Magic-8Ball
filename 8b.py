import tkinter
import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + \
        root.winfo_y()
    root.geometry("+%s+%s" % (x, y))
    Predict()

def Predict():
    with open('Languages\\'+languages[picker.current()]+'.txt', 'r') as file:
        quotes = file.read().splitlines()
    ft = random.choice(quotes)
    pred.configure(text=ft,fg="black")

root = Tk()
ball=Image.open("8Ball.png")
eb=ImageTk.PhotoImage(ball)

lbl=tkinter.Label(image=eb, bg='pink')
lbl.image=eb

lbl.place(x=0,y=0)
root.geometry('600x600')

sw = (root.winfo_screenwidth()/2)-300
sh = (root.winfo_screenheight()/2)-300

root.config(highlightbackground='pink')
root.geometry("+%d+%d" % (sw, sh))
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'pink')
pred=tkinter.Label(width=30,height=1,text='Shake to get your fortune!',fg='grey',bg='lightgrey')
pred.place(x=190, y=250)
languages=["en","es","fr","ge","pt"]
picker=ttk.Combobox(values=languages,width=2,height=5)
picker.set("en")
picker.place(x=410,y=250)
qit=tkinter.Button(width=11,bg='darkgrey',text="Quit",command=root.destroy)
qit.place(x=260,y=280)
root.bind('<Button-1>', SaveLastClickPos)
root.bind('<B1-Motion>', Dragging)
root.mainloop()
