import pytest
import src.RPS_spock_lizard as game

def test_draw():
    assert game.GameResult.Tie == game.assess_game(
        user_action=game.GameAction.Spock, 
        computer_action=game.GameAction.Spock)
    
    assert game.GameResult.Tie == game.assess_game(
        user_action=game.GameAction.Lizard, 
        computer_action=game.GameAction.Lizard)

    assert game.GameResult.Tie == game.assess_game(
        user_action=game.GameAction.Rock, 
        computer_action=game.GameAction.Rock)

    assert game.GameResult.Tie == game.assess_game(
        user_action=game.GameAction.Scissors, 
        computer_action=game.GameAction.Scissors)

    assert game.GameResult.Tie == game.assess_game(
        user_action=game.GameAction.Paper, 
        computer_action=game.GameAction.Paper)


def test_spock_loses():
    '''
    Spock pierde con Lizard y Paper 
    '''
    assert game.GameResult.Victory == game.assess_game(
        user_action=game.GameAction.Paper, 
        computer_action=game.GameAction.Spock)

    assert game.GameResult.Victory == game.assess_game(
        user_action=game.GameAction.Lizard, 
        computer_action=game.GameAction.Spock)


def test_spock_wins():
    '''
    Spock gana a Rock y Scissors 
    '''
    assert game.GameResult.Defeat == game.assess_game(
        user_action=game.GameAction.Rock, 
        computer_action=game.GameAction.Spock)

    assert game.GameResult.Defeat == game.assess_game(
        user_action=game.GameAction.Scissors, 
        computer_action=game.GameAction.Spock)


def test_lizard_loses():
    '''
    Lizard pierde con Rock y Scissors 
    '''
    assert game.GameResult.Victory == game.assess_game(
        user_action=game.GameAction.Rock, 
        computer_action=game.GameAction.Lizard)

    assert game.GameResult.Victory == game.assess_game(
        user_action=game.GameAction.Scissors, 
        computer_action=game.GameAction.Lizard)


def test_lizard_wins():
    '''
    Lizard gana a Spock y Paper 
    '''
    assert game.GameResult.Defeat == game.assess_game(
        user_action=game.GameAction.Spock, 
        computer_action=game.GameAction.Lizard)

    assert game.GameResult.Defeat == game.assess_game(
        user_action=game.GameAction.Paper, 
        computer_action=game.GameAction.Lizard)







