# simple password Generator
import random
import time
from characters import character

characters = character

number = input('Number of passwords? - ')                
number = int(number)

time.sleep(1)

length = input('How many characters? - ')
length = int(length)

time.sleep(0.5)

print("Generating passwords...")

time.sleep(1)

for p in range(number):
  password = ''
  for c in range(length):
    password += random.choice(characters)
  print("password :- " + password)

time.sleep(1)

print("Passwords have been generated!")

time.sleep(1)

print("Thank you for using the MatrixDev password generator.")
