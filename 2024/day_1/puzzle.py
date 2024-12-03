total_distance = 0
total_similarity = 0
list_one = []
list_two = []

# read the input and split it into two lists
with open('./input.txt', 'r') as f:
    for line in f:
        values = ' '.join(line.split()).split(' ')
        list_one.append(int(values[0]))
        list_two.append(int(values[1]))

# sort the lists from smallest to largest
list_one.sort(), list_two.sort()

# loop through each number and find the absolute value of distance between the two
for index, num in enumerate(list_one):
    total_distance += abs(num - list_two[index])

# puzzle one answer
print('Puzzle One Answer: ', total_distance)

# loop through the lists and find the similarity value between matching numbers
for num in list_one:
    if num >= list_two[0]:
        # count the amount of times it shows up
        count = 0
        for index, num_two in enumerate(list_two):
            if num_two > num:
                list_two = list_two[index:]
                break
            if num_two == num:
                count += 1
        total_similarity += count * num

# puzzle two answer
print('Puzzle Two Answer: ', total_similarity)