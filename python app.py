from tkinter import *

window = Tk()
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)
window.title("TO-DO APP")
window.config(bg= "blue")
l1 = Label(window, text="TO-DO App", fg="blue", bg="pink", font="caliber 12 bold").pack(fill=X)


content = StringVar()

e1 = Entry(window, textvariable=content, width=25, font="caliber 12 bold")
e1.pack(pady=5)



def add():
    lb1.insert(END, content.get())
    content.set("")

b1 = Button(window, text="Enter", bg="pink", fg="black", width=8, command=add)
b1.pack()

scollbar = Scrollbar(window)
scollbar.pack(side=RIGHT,fill=Y)

lb1 = Listbox(window,yscrollcommand=scollbar.set, width=40, height=15, bg="pink", fg="blue", font="caliber 9 bold")
lb1.pack(pady = 15)

scollbar.config(command= lb1.yview)
def remove():
    lb1.delete(ANCHOR)

b2 = Button(window, text="Delete", bg="pink", fg="black", width=8, command=remove)
b2.place(x=210, y=360)


b3 = Button(window, text="Exit", bg="pink", fg="black", width=8, command=exit)
b3.place(x=100, y=360)


window.mainloop()