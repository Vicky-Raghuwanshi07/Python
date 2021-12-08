import random

print('\t\t\t\tRock Paper Scissor\n')
print("1.Rock\n2.Paper\n3.Scissor\n\n")

USER = 0
CPU = 0
TIE = 0
i =1

while i<=5:
    choice = int(input('Enter your choice : '))
    if choice>=1 and choice<=3:
        computer = random.randint(1,3)
        if ((choice==1 and computer==3) or (choice==2 and computer==1) or (choice==3 and computer==2)):
            print("Congrats you win\n")
            USER+=1
        elif ((computer==1 and choice==3)or(computer==2 and choice==1)or(computer==3 and choice==2)):
            print("Computer win\n")
            CPU+=1
        else:
            print("Tie!!!\n")
            TIE+=1
        i+=1
    else:
        print("Enter a valid choice")
print(f"Total winnig\nYou win :{USER}\nComputer win :{CPU}\nTie Matches :{TIE}\n")
if USER>CPU:
	print("You win the series")
elif CPU>USER:
	print("Computer wins the series")
else :
	print("Series Tied!!!")