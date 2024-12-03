total_safe = 0
total_safe_damp = 0

def check_safety(report):
    safe = True
    index = 1
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
    return safe, index

# read the input and split it into two lists
with open('./input.txt', 'r') as f:
    for line in f:
        report = [int(num) for num in line.split(' ')]
        safe, index = check_safety(report)
        
        if safe:
            total_safe += 1
        else:
            for index, num in enumerate(report):
                # exlude that index
                sub_report = report[:index] + report[index + 1:]
                safe, index = check_safety(sub_report)
                if safe:
                    total_safe_damp += 1
                    break



# puzzle one answer               
print('Total Safe:', total_safe)
# puzzle two answer               
print('Total Safe with Dampener:', total_safe + total_safe_damp)