from tkinter import *

win = Tk()

subjects = ['physics', 'chemistry', 'maths']

def selectSub():
    print(lb.selection_get())

lb = Listbox(win, selectmode = 'multiple')
for i in subjects:
    lb.insert(END,i)
lb.pack()

btn = Button(win,text="show selection", command=selectSub)
btn.pack()

win.mainloop()