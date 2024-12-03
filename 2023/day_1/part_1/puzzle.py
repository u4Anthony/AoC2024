final_value = 0
file = open('./input.txt', 'r')
for line in file:
    for char in line:
        if char in '1234567890':
            first = char
            break
    for char in line[::-1]: # specify a slice with no ends, but stepping backwards
        if char in '1234567890':
            second = char
            break
    final_value += int(first + second)
file.close()
print(final_value)