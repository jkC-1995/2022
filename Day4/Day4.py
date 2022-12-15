with open('/Users/Jak.Bustin/Documents/AdventOfCode/2022/Day4/input.txt', 'r') as f:
    lines = f.readlines()
    line = [entry.strip() for entry in lines]


total = 0
total_2 = 0


def find_seq():
    return


for x in line:
    id_1 = []
    id_2 = []
    seq_1 = []
    seq_2 = []

    current_set = x.split(",")
    print("Current Line: ", current_set)
    n1 = str(current_set[0]).split("-")
    n2 = str(current_set[1]).split("-")

    print("Finding Sequence between: ", n1)

    for i in n1:
        id_1.append(int(i))

    print("Finding Sequence between: ", n2)

    for i in n2:
        id_2.append(int(i))

    # append sequence to list

    for i in range(id_1[0], id_1[1]+1):
        seq_1.append(i)
    print("First block Sequence: ", seq_1)

    for i in range(id_2[0], id_2[1]+1):
        seq_2.append(i)
    print("Second block Sequence: ", seq_2)

    print("-----Next Number Block---------")

    check = all(item in seq_1 for item in seq_2)
    check_2 = all(item in seq_2 for item in seq_1)

    if check is True:
        total += 1
    elif check_2 is True:
        total += 1

    # part2

    for item in seq_2:
        if item in seq_1:
            total_2 += 1
            break


# part 1 answer
print("Total overlaps Part 1: ", total)
print("Total single overlaps: ", total_2)

# part 2
