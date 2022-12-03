elves = open("input.txt").read().split("\n\n")

totals = []

for set in elves:
    current_set = set.split("\n")
    #print("current_set: ", current_set)

    answer = sum([int(x) for x in current_set])
    #print("Sum of current set: ", answer)
    totals.append(answer)


# print(max(totals))

# part 2

totals.sort()

print(sum(totals[-3:]))

# print(type(totals))


#top_3 = sorted(zip(totals), reverse=True)[:3]

# test
