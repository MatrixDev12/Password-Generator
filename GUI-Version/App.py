from tkinter import *

root = Tk()
root.title("Password Generator")

length = Entry.get(self)
length_to_int = int(length)
number = Entry.get(self)
number_to_int = int(number)

gen = Button(root,text="generator")
gen.pack()

root.mainloop()