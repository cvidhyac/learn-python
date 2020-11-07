import random

print('What is your name')
name = input()
print('Hello' + name + ', I am thinking of a number between 1-20')
secretNumber = random.randint(1, 20)
numberOfGuesses = 0
for numberOfGuesses in range(1, 7):
  print('Take a guess')
  guess = int(input())
  if secretNumber > guess:
    print('Guess is too low')
  elif secretNumber < guess:
    print('Guess is too high')
  else:
    print('Correct!')
    break

print('You took' + str(numberOfGuesses) + ' guesses.')
