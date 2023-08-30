from tkinter import *
root = Tk()
root.geometry('250x250')

leftbutton = Button(root,text="Left",fg="green")
leftbutton.pack(side=LEFT)
rightbutton = Button(root,text="Right",fg="Gray")
rightbutton.pack(side=RIGHT)
tb = Button(root,text="Top",fg="blue")
tb.pack(side=TOP)
bb = Button(root,text="Bottom",fg="red")
bb.pack(side=BOTTOM)

root.mainloop()
