import elements
import random
import time

print("\nDice Game - beat the computer score.\n")

time.sleep(3)

print("If you roll a 1 on either dice, your score will drop to 0.\n")

time.sleep(3)

play= (input("Press y to roll the dice.\n"))
playerScore=0
compScore=0


while play != "y":
  print("\nError.\n")
  play= (input("Press y to roll the dice.\n"))


while play == "y":

  time.sleep(1)

  
  roll=random.randint(0,5)
  print(elements.dice[roll])
  die1 = elements.dieScore[roll]

  
  
  roll=random.randint(0,5)
  print(elements.dice[roll])
  die2 = elements.dieScore[roll]

  if die1==1 or die2==1:
    playerScore=0
  else:
    playerScore += die1 + die2

  time.sleep(2)

  print("Computers turn to roll.\n")

  time.sleep(2)

  
  roll=random.randint(0,5)
  print(elements.dice[roll])
  die1 = elements.dieScore[roll]

  
  roll=random.randint(0,5)
  print(elements.dice[roll])
  die2 = elements.dieScore[roll]

  if die1==1 or die2==1:
    compScore=0
  else:
    compScore += die1 + die2

  time.sleep(2)
  print("Your score is: " + str(playerScore))

  time.sleep(2)

  print("The computer score is: " + str(compScore))
  play= (input("\nWould you like to roll again? y or n\n"))


if playerScore>compScore:
  print("\nYou won!")
else:
  print("\nYou lost!")

print("\nThanks for Playing. I hope you had fun!\n")

