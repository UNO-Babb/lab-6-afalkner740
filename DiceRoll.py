#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0]*13
  totalsum = 0
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolltotal = dice1 + dice2
    rolls[rolltotal] += 1
    totalsum += rolltotal

  #find the sum total of the two dice
  print("The Sum of the two die is:" ,totalsum)
  #print statictics for dice rolls
  dice = 1 
  for count in rolls:
    print ("Dice roll",dice, ": occurred", count, "times!")
    dice = dice +1

if __name__ == '__main__':
  main()
