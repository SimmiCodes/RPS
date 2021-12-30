from random import choice
l = ['rock','paper','scissor']

user = input("Enter ur choice")
system = choice(l)

print(user, system)

# user ask - yes or no
# score

if user == "rock":
    if system == 'rock':
        print("tie")
    elif system == 'paper':
        print("System win, you loose")
    else:
        print("You win")
elif user == "paper":
    if system == 'paper':
        print("tie")
    elif system == 'scissor':
        print("System win, you loose")
    else:
        print("You win")
else:
    if system == 'scissor':
        print("tie")
    elif system == 'rock':
        print("System win, you loose")
    else:
        print("You win")

