import random

number = random.randrange(0,20)


print('Pick a number between 0 and 20!')

guess = int(input("Pick a number: "))

if number == guess:
	print('The number is ' + str(number))
	print('You guessed the number correctly!')
elif guess > 20:
	print('Your guess is higher than 20')
else:
	print('The number is ' + str(number))
	print('You guessed incorrecyly!')