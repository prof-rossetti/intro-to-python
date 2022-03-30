








from app.game import determine_winner


def test_enlarge():
    assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    assert determine_winner(user_choice="rock", computer_choice="rock") == None
    assert determine_winner(user_choice="rock", computer_choice="scissors") == "rock"

    assert determine_winner(user_choice="paper", computer_choice="paper") == None
    assert determine_winner(user_choice="paper", computer_choice="rock") == "paper"
    assert determine_winner(user_choice="paper", computer_choice="scissors") == "scissors"

    assert determine_winner(user_choice="scissors", computer_choice="paper") == "scissors"
    assert determine_winner(user_choice="scissors", computer_choice="rock") == "rock"
    assert determine_winner(user_choice="scissors", computer_choice="scissors") == None
