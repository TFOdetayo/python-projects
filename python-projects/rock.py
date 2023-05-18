""" import random

exit = False
user_points = 0
computer_points = 0

while exit is False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print("You won a total score of "+str(user_points)+" and the computer's total score is "+str(computer_points))
        exit = True

    elif user_input == "rock":
        if computer_input ==  "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input ==  "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("computer wins!")
            computer_points += 1
        elif computer_input ==  "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win!")
            user_points += 1

    elif user_input == "paper":
        if computer_input ==  "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win!")
            user_points += 1
        elif computer_input ==  "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie!")
        elif computer_input ==  "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins!")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input ==  "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer wins!")
            computer_points += 1
        elif computer_input ==  "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            user_points += 1
        elif computer_input ==  "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It's a tie!")

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid Input!") """


"""import random

def play():

    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
        
    return 'You lost!'
    
    # r > s, s > p, p > r
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
    

print(play())"""