f = open("../password.txt", "r")
passwords = []
for i in f:
    passwords.append(i[:-1])
counter = 0
for i in passwords:
    set = i.split(':')
    rule, password = set[0], set[1]
    alpha, range = rule[-1], rule[:-1].strip().split('-')
    if (password[int(range[0])] == alpha or password[int(range[1])] == alpha) and (password[int(range[0])] != password[int(range[1])]):
        counter = counter + 1
print(counter)
