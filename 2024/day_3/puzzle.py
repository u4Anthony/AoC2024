import re

total_mul = 0
pattern = r'mul\(\d{1,3},\d{1,3}\)'
with open('./input.txt', 'r') as f:
    for line in f:
        temp_instr = ''
        for char in line:
            temp_instr += char
            match = re.search(pattern, temp_instr)
            if match:
                num_list = list(map(int, match.group(0)[4:-1].split(',')))
                total_mul += num_list[0] * num_list[1]
                temp_instr = ''

# puzzle one answer               
print('Total Value 1:', total_mul)

total_mul = 0
do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'
with open('./input.txt', 'r') as f:
    for line in f:
        temp_instr = ''
        do = False
        dont = True
        for char in line:
            temp_instr += char
            if re.search(dont_pattern, temp_instr):
                do = False
                dont = True
                temp_instr = temp_instr[temp_instr.find('don\'t()'):]
            if re.search(do_pattern, temp_instr):
                do = True
                dont = False
                temp_instr = temp_instr[temp_instr.find('do()'):]
            if do:
                match = re.search(pattern, temp_instr)
                if match:
                    print(temp_instr)
                    print(match.group(0), '\r\n')
                    num_list = list(map(int, match.group(0)[4:-1].split(',')))
                    total_mul += num_list[0] * num_list[1]
                    temp_instr = ''
                

# puzzle one answer               
print('Total Value 2:', total_mul)