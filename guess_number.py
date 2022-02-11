import random
num1 = random.randint(1 , 10)
guess = int(input("guess a number between 1 to 10\n"))
while guess !=num1:
      print("sorry, try again\n")
      guess = int(input("guess a number between 1 to 10\n"))
print("Congratulations! you have won the game")


