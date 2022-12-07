with open('/Users/Jak.Bustin/Documents/AdventOfCode/2022/Day3/input.txt', 'r') as f:
    lines = f.readlines()
    rucksack = [entry.strip() for entry in lines]


lowercase = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
             "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


uppercase = {"A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39,
             "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}


def sum_letters(letter):

    if letter.islower():
        lower_case = lowercase[letter]
        return lower_case
    elif letter.isupper():
        upper_case = uppercase[letter]
        return upper_case


common_characters = []

for x in rucksack:
    first_half = set(x[:len(x)//2])
    second_half = set(x[len(x)//2:])
    # get overlap through set logic (intersection of two sets)
    # intersection() return what in in first/second half
    overlap_char = (first_half.intersection(second_half)).pop()
    common_characters.append(overlap_char)


# part 1 answer

print(sum([sum_letters(letter) for letter in common_characters]))

# part 2

# split rucksack in to lines of 3

n = 3

common_characters2 = []

rucksack_group3 = [rucksack[i:i+n] for i in range(0, len(rucksack), n)]

# find common letter in the three lines

for x in rucksack_group3:
    print(x)
    common = set.intersection(*map(set, x)).pop()
    print(common)
    common_characters2.append(common)

# sum value of each letter like in part 1

print(sum([sum_letters(letter) for letter in common_characters2]))
