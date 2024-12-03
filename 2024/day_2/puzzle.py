total_safe = 0
total_safe_damp = 0

def check_safety(report):
    safe = True
    index = 1
    asc, dsc = False, False
    while index < len(report):
        if report[0] < report[1]:
            # ascending
            asc = True
            distance = report[index] - report[index - 1]
            if distance >= 4 or 0 >= distance:
                safe = False
                break
        else:
            # descending
            dsc = True
            distance = report[index - 1] - report[index]
            if distance >= 4 or 0 >= distance:
                safe = False
                break
        index += 1
    return safe, index, asc, dsc

# read the input and split it into two lists
with open('./input.txt', 'r') as f:
    for line in f:
        report = [int(num) for num in line.split(' ')]
        safe, index, asc, dsc = check_safety(report)
        
        if safe:
            total_safe += 1
        else:
            if asc:
                print('ASC', report, index)
            if index == 1:
                del report[0]
            else:
                del report[index - 1]
            safe, index, asc, dsc = check_safety(report)
            if asc:
                print('ASC', report, index, safe, '\r\n')
            if safe:
                total_safe += 1


# puzzle one answer               
print('Total Safe:', total_safe)
# puzzle two answer               
print('Total Safe with Dampener:', total_safe)