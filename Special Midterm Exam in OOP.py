from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry('600x600+20+10')


def bgchange():
    btn.configure(bg="yellow")


btn = Button(window, text="Click to Change Color", command=bgchange)
btn.place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()

