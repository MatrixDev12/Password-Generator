# simple password Generator
import random
from time import sleep
from characters import character

characters = character

number = input('Number of passwords? - ')                
number = int(number)

sleep(1)

length = input('How many characters? - ')
length = int(length)

sleep(0.5)

print("Generating passwords...")

sleep(1)

for p in range(number):
  password = ''
  for c in range(length):
    password += random.choice(characters)
  print("password :- " + password)

sleep(1)

print("Passwords have been generated!")

sleep(1)

print("Thank you for using the MatrixDev password generator.")
