from tkinter import *

win = Tk()
equation = ' '

def click(n):
    global equation
    equation += n
    e1.delete(0,END)
    e1.insert(0,equation)

def calculate():
    global equation
    equation = eval(equation)
    e1.delete(0,END)
    e1.insert(0,equation)

e1 = Entry(win)

e1.grid(row=1,column=1,columnspan=4)
btn = Button(win, text="7", command=lambda : click('7'))
btn.grid(row=2,column=1)
btn = Button(win, text="8", command=lambda : click('8'))
btn.grid(row=2,column=2)
btn = Button(win, text="9", command=lambda : click('9'))
btn.grid(row=2,column=3)
btn = Button(win, text="+", command=lambda : click('+'))
btn.grid(row=2,column=4)

btn = Button(win, text="4", command=lambda : click('4'))
btn.grid(row=3,column=1)
btn = Button(win, text="5", command=lambda : click('5'))
btn.grid(row=3,column=2)
btn = Button(win, text="6", command=lambda : click('6'))
btn.grid(row=3,column=3)
btn = Button(win, text="-", command=lambda : click('-'))
btn.grid(row=3,column=4)

btn = Button(win, text="1", command=lambda : click('1'))
btn.grid(row=4,column=1)
btn = Button(win, text="2", command=lambda : click('2'))
btn.grid(row=4,column=2)
btn = Button(win, text="3", command=lambda : click('3'))
btn.grid(row=4,column=3)
btn = Button(win, text="*", command=lambda : click('*'))
btn.grid(row=4,column=4)

btn = Button(win, text=".", command=lambda : click('.'))
btn.grid(row=5,column=1)
btn = Button(win, text="0", command=lambda : click('0'))
btn.grid(row=5,column=2)
btn = Button(win, text="00", command=lambda : click('00'))
btn.grid(row=5,column=3)
# btn = Button(win, text="/", command=lambda : click('/'))
btn = Button(win,text="=",command=calculate)
btn.grid(row=5,column=4)

win.mainloop()