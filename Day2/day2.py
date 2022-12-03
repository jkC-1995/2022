# A for Rock, B for Paper, and C for Scissors
# response: X for Rock, Y for Paper, and Z for Scissors.

# Score: 0 if you lost, 3 if the round was a draw, and 6 if you won +
# (1 for Rock, 2 for Paper, and 3 for Scissors)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    hands = [entry.strip() for entry in lines]

print(hands)


map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
             'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}


def points_per_round(choice):
    opponent_shape = map_input[choice[0]]
    our_shape = map_input[choice[2]]

    if opponent_shape == our_shape:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]

    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[our_shape]

    return 0


print(sum([points_per_round(choice) for choice in hands]))
