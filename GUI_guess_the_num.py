import tkinter as tk
from tkinter import *
import random
window = tk.Tk()
window.geometry("600x400+500+150")
window.minsize(600,400)
window.maxsize(1200,800)
window.config(bg="#ff0000")
window.resizable(width=True,height=True)
window.title('Guess The Number')
# You can add your own application icon by adding the below lines of code and give the image/icon path in PhotoImage()
# p1 = PhotoImage(file="PATH")
# window.iconphoto(True,p1)
TARGET = random.randint(0, 50)
RETRIES = 0

def update_result(text):
    result.configure(text=text)


def new_game(event):
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 50)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 50")

def play_game(event):
    global RETRIES

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1

        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "The required number lies between 0 and {}".format(choice)
        else:
            hint = "The required number lies between {} and 50".format(choice)
        result += "\n\nHINT :\n" + hint

    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)


title = tk.Label(window,text="Guess The Number",font=("Arial",24),fg="#fffcbd",bg="#065569")

result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)

play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "#000000", bg="#29c70a", command=new_game)
## Whenever a user press the Space key the game will refresh and start the new game
window.bind('<space>',new_game)

guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
## Here Enter key is used as a Guess Button
window.bind('<Return>', play_game)

exit_button = tk.Button(window,text="Exit Game",font=("Arial",14), fg="#ffffff", bg="#b82741", command=exit,)
## Using Escape to quit/exit from the game window
window.bind('<Escape>',exit)

guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)

title.place(x=170, y=50)
result.place(x=180, y=210)

exit_button.place(x=300,y=320)
guess_button.place(x=350, y=147) 
play_button.place(x=170, y=320)

number_form.place(x=180, y=150)

window.mainloop()