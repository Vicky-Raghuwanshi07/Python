from words import word    ### this will import a word list from words.py which contains number of words
from hangman_draw import lives_draw   ### this will shows the progress and lives
import random 
import string

def guess_words(word):
	g_word = random.choice(word)     ## choosing random word from words.py
	if "-" in g_word or " " in g_word:
		g_word = random.choice(word)
	
	return g_word.upper()
	
def hangman():
	s_word = guess_words(word)
	set_word = set(s_word)
	alphabet = set(string.ascii_uppercase)
	used_word = set()
	lives = 5
	while len(set_word)>0 and lives>0:
		print(lives_draw[lives])
		print("\n\n")
		word_letter = [l if l in used_word else "-" for l in s_word]
		print("Word : "+ " ".join(word_letter))
		print("You have remaining lives are : ",lives, "\nYour guessed letters are : ", " ".join(used_word))
		user = input("Current Letter : ").upper()
		
		if user in alphabet - used_word:
			used_word.add(user)
			if user in set_word:
				set_word.remove(user)
			else:
				lives-=1
				print("Lives : ",lives)
		elif user in used_word:
			print("Already used this charater , plz type diffrent charater ")
			print()
		
		else:
			print("Invalid input")
			print()
		
			
	if lives==0:
		print("\n\n")
		print(lives_draw[lives])
		print("\nSorry , You Loss\nThe right word is : ",s_word)
	else:
		print("\nYaah!! Correct guessed , The Word is :", s_word)
		
if __name__ == "__main__":
	print("Welcome To Hangman Game".center(54,"-"))
	hangman()
