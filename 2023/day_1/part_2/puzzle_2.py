NUMBERS = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
final_value = 0
file = open('./input.txt', 'r')
for line in file:
    line_numbers = []
    temp_string = ''
    for char in line:
        if char in '1234567890':
            line_numbers.append(char)
        else:
            temp_string += char
            for num_string in NUMBERS:
                if num_string in temp_string:
                    line_numbers.append(str(NUMBERS.index(num_string)))
                    temp_string = char
    final_value += int(line_numbers[0] + line_numbers[-1])
file.close()
print(final_value)