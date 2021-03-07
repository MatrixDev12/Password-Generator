from tkinter import *
from random import choice
from chars import characters

pgen = Tk()
pgen.geometry('300x300')
pgen.title("Password Generator")
lbl1 = Label(pgen, text="Password Generator")
lbl1.pack()

lbl2 = Label(pgen, text="Choose a password strength").pack()

def weak():   
    pw = ''
    for c in range(4):
        pw += choice(characters)
    weak = Label(pgen,text=pw).pack(pady=5)

def moderate():   
    pw = ''
    for c in range(8):
        pw += choice(characters)
    moderate = Label(pgen,text=pw).pack(pady=5)

def strong():   
    pw = ''
    for c in range(12):
        pw += choice(characters)
    strong = Label(pgen,text=pw).pack(pady=5)

def strongest():   
    pw = ''
    for c in range(14):
        pw += choice(characters)
    strongest = Label(pgen,text=pw).pack(pady=5)

btn = Button(pgen,text="Weak",command=weak).pack(pady=5)
btn1 = Button(pgen,text="Moderate",command=moderate).pack(pady=5)
btn2 = Button(pgen,text="Strong",command=strong).pack(pady=5)
btn3 = Button(pgen,text="Strongest",command=strongest).pack(pady=5)

lbl3 = Label(pgen,text="Result").pack()

pgen.mainloop()

