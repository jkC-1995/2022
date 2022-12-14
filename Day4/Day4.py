with open('/Users/Jak.Bustin/Documents/AdventOfCode/2022/Day4/input.txt', 'r') as f:
    lines = f.readlines()
    line = [entry.strip() for entry in lines]


total = 0

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

# part 1 answer
print("Total overlaps Part 1: ", total)


# read in each ID in pairs of 2

# put each ID in to a list start at first numberical number and ending at second

# compare the lists with eachother to see if list 1 is covered by list 2


'''
  num1 = int(current_set[0][0])
    num2 = int(current_set[0][2:])

    print("Num1: ", num1)
    print("Num2", num2)

    for i in range(num1, num2+1):
        id_1.append(i)
    print("ID 1: ", id_1)

    num3 = int(current_set[1][0])
    num4 = int(current_set[1][2:])

    for i in range(num3, num4+1):
        id_2.append(i)

    print("ID 2: ", id_2)
'''
