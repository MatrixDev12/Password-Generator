# simple password Generator
from random import choice as ch
from time import sleep as s
from characters import characters

number = input('Number of passwords? - ')                
number = int(number)

s(1)

length = input('How many characters? - ')
length = int(length)

for p in range(number):
  pw = ''
  for c in range(length):
    pw += ch(characters)
  print("Password = " + pw)


