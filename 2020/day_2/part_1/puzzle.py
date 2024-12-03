f = open("../password.txt", "r")
passwords = []
for i in f:
    passwords.append(i[:-1])
counter = 0
for i in passwords:
    set = i.split(':')
    rule, password = set[0], set[1]
    alpha, range = rule[-1], rule[:-1].strip().split('-')
    if password.count(alpha) >= int(range[0]) and password.count(alpha) <= int(range[1]):
        counter = counter + 1
print(counter)
