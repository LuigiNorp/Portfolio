def flip_coin():
    """
    It choose randomly if the value is 'heads' or 'tails'.
    :return: 'Heads' or 'tails'.
    """
    from random import choice
    moves = ['head', 'tails']
    return choice(moves)


def tossing_thecoin(player1_points=0, player2_points=0):
    """
    Simulates a single turn of the "heads or tails" game. The turn provides for both player 1
    and player 2 to choose an option each ones.
    :param player1_points: Quantity of player 1's winning points at moment
    :param player2_points: Quantity of player 2's winning points at moment
    :return: *  If player 1 wins his turn and opposite's turn, returns p1points +2
             *  If player 1 wins his turn and opposite wins its turn,
                returns p1points +1  and p2points +1 (and vice versa)
             *  If player 2 wins its own and opposite's turn, returns p2points +2

    """
    # Player 1 Turn
    coin = flip_coin()
    player = flip_coin()

    if player == coin:
        player1_points += 1
        print("Player 1:", player1_points)
    else:
        player2_points += 1
        print("Player 2:", player2_points)

    # Player 2 Turn
    coin = flip_coin()
    player = flip_coin()
    if player == coin:
        player2_points += 1
    else:
        player1_points += 1
        print("Player 1:", player1_points)

    return player1_points, player2_points


def final_score(p1points=0, p2points=0, round_num=0):
    """
    Shows the final score. It shows you if player 1, or player 2 wins, and if they draw. And plus,
    shows the total rounds played.
    :param p1points: Quantity of player 1's winning points at moment.
    :param p2points: Quantity of player 2's winning points at moment.
    :param round_num: Input the value of the total number of rounds.
    :return: It do not return a value
    """
    if p1points > p2points:
        print("\n----------------------------  Player 1 wins  ----------------------------")
        print("Player 1:", p1points, "points")
        print("Player 2:", p2points, "points")
    elif p2points > p1points:
        print("\n----------------------------  Player 2 wins  ----------------------------")
        print("Player 1:", p1points, "points")
        print("Player 2:", p2points, "points")
    else:
        print("\n----------------------------      Draw      ----------------------------")
        print("Player 1:", p1points, "points")
        print("Player 2:", p2points, "points")

    print("Total rounds:", round_num)