# Author: Edoardo Gozzi
# Created: 27/03/2022

import random
from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk

def app():
    root=Tk()
    root.title("Dice Simulator")
    root.geometry('200x130')
    root.resizable(False,False)
    root.config(bg='white')

    def roll():
        path = str(Path.home() / "DCsim/dices")
        num=random.randint(1,6)
        value=str(num)
        img=Image.open(path+'/dice '+value)
        img=img.resize((50,50), Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        panel=Label(root,image=img,bd=0)
        panel.image=img
        panel.place(x=75,y=50)
    b=Button(root,text='Throw',bg="white",fg="black",width=5,border=0,highlightthickness=0,bd=0,activebackground='white',command=roll)
    b.place(x=65,y=4)
    root.mainloop()
app()
