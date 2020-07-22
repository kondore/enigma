#This is a guess the number game
import random

print('Hello. What is your name?')
name = input()

secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20...')


for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break #this condition is met when guess is correct, or too many guesses taken, and will now break out of the loop

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')

