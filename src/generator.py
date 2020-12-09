# simple password Generator
from random import choice
from time import sleep as s
from characters import character

characters = character

number = input('Number of passwords? - ')                
number = int(number)

s(1)

length = input('How many characters? - ')
length = int(length)

s(0.5)

print("Generating passwords...") 

s(1)

for p in range(number):
  password = ''
  for c in range(length):
    password += choice(characters)
  print("password :- " + password)

s(1)

print("passwords have been generated!")

print(number)

s(1)

print("Thank you for using the MatrixDev password generator.")
