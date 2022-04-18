expenses = [100, 250, 300, 1000, 3100, 50, 450]
total = 0
# for item in expenses:
#     total = total + item

print(total)

# range function

for i in range(1, 11):

    if i == 3:
        continue

    elif i == 7:
        break
    print(i)

for i in range(len(expenses)):
    print('Month: ', (i + 1), 'Expense: ', expenses[i])
    total = total + expenses[i]

print('Total expenses is:', total)

x = 1
while x <= 5:
    print(x)
    x = x + 1
