import random

x = random.randrange(1,10)

guess = int(input('Guess a number between 1 and 10: '))

if guess < x:
    print('You lose, the number was higher.')
elif guess > x:
    print('You lose, the number was lower.')
else:
    print(f'You win! the number was {x}')