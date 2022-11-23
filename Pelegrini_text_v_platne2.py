import tkinter
from random import *
canvas = tkinter.Canvas(width=500,height=100)
canvas.pack()

def slovo():
    global slovo
    slovo=(entry1.get())
    farba=' '
    x=0
    for i in range(len(slovo)):
        x=x+25
        if i%2==0:
            canvas.create_text(100+x,50,text=slovo[i],font='Arial 35')
        if i%2==1:
            canvas.create_text(100+x,70,text=slovo[i],font='Arial 35')

entry1 = tkinter.Entry() 
entry1.pack()

button1 = tkinter.Button(text='ok',command=slovo)
button1.pack()