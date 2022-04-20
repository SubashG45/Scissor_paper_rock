import random

user_wins = 0
computer_wins = 0

options = ['rock', "paper", "scissor"]

while True:
    user_input = input('Input Rock\Paper\Scissor or Q to quit: ').lower()
    if user_input == "q":
        break
    if user_input not in  options:
        continue

    random_number = random.randint(0,2)

    computer_pick = options[random_number]
    print("computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Win")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You Win")
        user_wins += 1
        continue
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Win")
        user_wins += 1
        continue
    else:
        print("You lose")
        computer_wins += 1

print("YOU WON", user_wins, "times")
print("Computer wins", computer_wins, "times")
print('GoodBye!')



