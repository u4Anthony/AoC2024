file = open("../input.txt", "r")
expenses = []
for x in file:
    expenses.append(x[:-1])
print(expenses)
for x in expenses:
    for y in expenses:
        for z in expenses:
            if (int(x) + int(y) + int(z) == 2020):
                print(int(x) * int(y) * int(z))
                break
