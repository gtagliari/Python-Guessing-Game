# setting up global variables
import random
print("Welcome! Try to Guess the Number!")
numGuess = 0
reset = 2
print("The number is generated randomly from 1-25")
randomNum = random.randint(0,25)

while True:
	try:
		guess = int(input("Enter a number between 1-25: "))
		try:
			if(guess >= 1 and guess <= 25):
				# check if the guess is above the random number
				if(guess > randomNum):
					print("Number is too high")
					numGuess += 1
					continue
				# check if the guess is below the random number
				elif(guess < randomNum):
					print("Number is too low")
					numGuess += 1
					continue
				# the player wins the game and shows score 
				else:
					numGuess += 1
					print("You got it")
					print("You took " + str(numGuess) + " guesses to get it correct")
					reset = int(input("Type 0 to reset the game or type -1 to quit the game: "))
					# resetting the game function					
					if(reset == 0):
						randomNum = random.randint(0,25)
						numGuess = 0
						reset = 2
					# completely closes the game
					if(reset == -1):
						break
			else:
				print("Make sure your guess is between 1-25")
		# making sure the inout is an integer 
		except ValueError:
			print("Make sure your guess is an integer")
	except ValueError:
		print("Make sure your guess is an integer")
		