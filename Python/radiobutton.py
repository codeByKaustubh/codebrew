from tkinter import *

win = Tk()

def submitForm():
    print(gender.get(),check.get())

l1 = Label(win, text="gender")
l1.pack()

gender = StringVar()
r1 = Radiobutton(win, text="Male", value="male", variable=gender)
r1.pack()
r2 = Radiobutton(win, text="Female", value="female", variable=gender)
r2.pack()
r1.select()

check = StringVar()
c1 = Checkbutton(win, text="I agree to the T&C", onvalue="I agree", offvalue="I disagree", variable=check)
c1.pack()

btn=Button(win, text="submit", command=submitForm)
btn.pack()

win.mainloop()