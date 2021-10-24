import random
def guess(guess_no,i):
	"""guess(GuessNo) --> A random number from 1-50 is genrated"""
	while i<=5:
		num = int(input('Guess the no.:'))
		if (num<1 or num>50):
			print('OutOfRange!!! Please enter a valid 	number\n')
			continue
		elif num>guess_no:
			print('Your guess is too high\n')
		elif num<guess_no:
			print('Your guess is too low\n')
		else:
			print('Congo!! You guessed it right. The no. is ',guess_no)
			break
		i+=1
	if i>5:
		print('\nSorry!! You have lost all chances to guess the number')
		print('\nThe number is:',guess_no)
		return 0
if __name__=='__main__':
	i = 1
	print('\t\t\t\t\tGUESS THE NUMBER!!!\n')
	print('\t\t\t\tYou have 5 chances to guess the number\n')
	guess_no = random.randint(1,50)
	guess(guess_no,i)