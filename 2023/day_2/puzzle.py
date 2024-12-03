def main():
    part_one()
    part_two()

def part_one():
    file = open('./input.txt', 'r')
    final_sum = 0
    for index, line in enumerate(file):
        line = line.split(': ',1)[1].split(';')
        good_line = True
        for handful in line:
            handful_vals = handful.strip().split(', ')
            for check in handful_vals:
                if 'red' in check and int(check.split(' ')[0]) > 12:
                    good_line = False
                elif 'green' in check and int(check.split(' ')[0]) > 13:
                    good_line = False
                elif 'blue' in check and int(check.split(' ')[0]) > 14:
                    good_line = False
        if good_line == True:
            final_sum += index + 1
    file.close()
    print(f'Final Sum = {final_sum}')

def part_two():
    file = open('./PuzzleInput.txt', 'r')
    final_sum = 0
    for index, line in enumerate(file):
        line = line.split(': ',1)[1].split(';')
        red_value = 0
        green_value = 0
        blue_value = 0
        good_line = True
        for handful in line:
            handful_vals = handful.strip().split(', ')
            for check in handful_vals:
                if 'red' in check:
                    if int(check.split(' ')[0]) > red_value:
                        red_value = int(check.split(' ')[0])
                elif 'green' in check:
                    if int(check.split(' ')[0]) > green_value:
                        green_value = int(check.split(' ')[0])
                elif 'blue' in check:
                    if int(check.split(' ')[0]) > blue_value:
                        blue_value = int(check.split(' ')[0])
        if good_line == True:
            final_sum += (red_value * green_value * blue_value)
    file.close()
    print(f'Final Sum = {final_sum}')

if __name__ == '__main__':
    main()