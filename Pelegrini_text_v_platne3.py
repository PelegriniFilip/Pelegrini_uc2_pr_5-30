import tkinter
from random import *
canvas = tkinter.Canvas(width=500,height=100,bg='white')
canvas.pack()

def slovo():
    global slovo
    slovo=(entry1.get())
    farba='blue'
    x=0
    canvas.delete(all)
    for i in range(len(slovo)):
        x=x+25
        canvas.create_text(100+x,50,text=slovo[i],font='Arial 35')
        canvas.after(1000)

entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='ok',command=slovo)
button1.pack()