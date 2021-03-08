from characters import characters
from random import choice

inpt = input("Input desired password strength (weak, moderate, strong, strongest, custom) ")

def weak():   
    pw = ''
    for c in range(4):
        pw += choice(characters)
    print("Password = " + pw)

def moderate():   
    pw = ''
    for c in range(8):
        pw += choice(characters)
    print("Password = " + pw)

def strong():   
    pw = ''
    for c in range(12):
        pw += choice(characters)
    print("Password = " + pw)

def strongest():   
    pw = ''
    for c in range(14):
        pw += choice(characters)
    print("Password = " + pw)


def custom():
    length = input('How many characters? - ')
    length = int(length)

    pw = ''
    for c in range(length):
        pw += choice(characters)
    print("Password = " + pw)

if inpt == "weak":
    weak()

if inpt == "moderate":
    moderate()

if inpt == "strong":
    strong()

if inpt == "strongest":
    strongest

if inpt == "custom":
    custom()


