import random

def get_choices():
    player_choice = input(" Enter a choice between rock, paper, and scissors: ")

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print("Player chose " + player + ", and the computer chose " + computer)
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smahses scissors! You Win"
        else:
            return "Paper beats rock! You lose"

    elif player == "paper":
        if computer == "rock":
            return "Paper beats rock! You Win"
        else:
            return "scissors cut paper! You lose"

    elif player == "scissors":
        if computer == "paper":
            return "scissors beats paper! You Win"
        else:
            return "rock cut scissors! You lose"


choices = get_choices()
results = check_win(choices["player"], choices["computer"])
print(results)