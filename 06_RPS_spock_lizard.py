#!/usr/bin/python3

import random
from enum import IntEnum
from statistics import mode


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    # Spock = 3


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock,
    # GameAction.Spock: GameAction.Paper
}


NUMBER_RECENT_ACTIONS = 5


def assess_game(user_action, computer_action):
    game_result = None
    
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie
    elif Victories[user_action] == computer_action:
        print("%s wins %s. You lost!" %(computer_action.name, user_action.name))
        game_result = GameResult.Defeat
    else:
        print("%s wins %s. You win!" %(user_action.name, computer_action.name))
        game_result = GameResult.Victory

    return game_result

            
def get_computer_action(user_actions_history, game_history):
    # No previous user actions => random computer choice
    if not user_actions_history or not game_history:
        computer_action = get_random_computer_action()
    # Alternative AI functionality
    # Choice that would beat the user's most frequent recent choice
    else:
        most_frequent_recent_computer_action = GameAction(mode(user_actions_history[-NUMBER_RECENT_ACTIONS:]))
        computer_action = get_winner_action(most_frequent_recent_computer_action)

    print(f"Computer picked {computer_action.name}.")
    
    return computer_action
            

def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)
       
    return user_action


def get_random_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)

    return computer_action


def get_winner_action(game_action):
    return Victories[game_action]


def play_another_round():
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'
        

def main():
    game_history = []
    user_actions_history = []
    
    while True:
        computer_action = get_computer_action(user_actions_history, game_history)
        
        try:
            user_action = get_user_action()
            user_actions_history.append(user_action)
        except ValueError as e:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue


        game_result = assess_game(user_action, computer_action)
        game_history.append(game_result)

        if not play_another_round():
            break
        

if __name__ == "__main__":
    main()
