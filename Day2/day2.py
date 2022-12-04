# A for Rock, B for Paper, and C for Scissors
# response: X for Rock, Y for Paper, and Z for Scissors.

# Score: 0 if you lost, 3 if the round was a draw, and 6 if you won +
# (1 for Rock, 2 for Paper, and 3 for Scissors)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    hands = [entry.strip() for entry in lines]


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


print("Part 1: ")
print(sum([points_per_round(choice) for choice in hands]))

map_input2 = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
              'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape2 = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome2 = {'Lose': 0, 'Draw': 3, 'Win': 6}


def part2(choice):
    opponent_shape = map_input2[choice[0]]
    game_result = map_input2[choice[2]]

    # if game result is draw:

    if game_result == 'Draw':
        return points_per_outcome2[game_result] + points_per_shape2[opponent_shape]

    elif game_result == 'Lose':
        if opponent_shape == 'Paper':
            return points_per_outcome2[game_result] + points_per_shape2['Rock']
        if opponent_shape == 'Rock':
            return points_per_outcome2[game_result] + points_per_shape2['Scissors']
        if opponent_shape == 'Scissors':
            return points_per_outcome2[game_result] + points_per_shape2['Paper']

    elif game_result == 'Win':
        if opponent_shape == 'Scissors':
            return points_per_outcome2[game_result] + points_per_shape2['Rock']
        if opponent_shape == 'Paper':
            return points_per_outcome2[game_result] + points_per_shape2['Scissors']
        if opponent_shape == 'Rock':
            return points_per_outcome2[game_result] + points_per_shape2['Paper']


# Day2
game_ending = {'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}

print("Part2: ")
print(sum([part2(choice) for choice in hands]))

# determine if need to win, lose or draw


# x lose, y draw, z win
