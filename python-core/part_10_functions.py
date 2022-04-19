# function make code more modular and readable

tom_expense_list = [2100, 3400, 3500]
joe_expense_list = [200, 500, 700]

total = 0
for item in tom_expense_list:
    total = total + item
print("Tom's total expense:", total)

total = 0
for item in joe_expense_list:
    total = total + item
print("Joe's total expense:", total)


# the problem with this aproach is that we we repeating code
# imagine if we had 1000 records to compute totals

def calculate_total(exp):
    """
    This function computes total expenses
    :param exp:
    :return: total
    """
    total = 0  # local variable
    for item in exp:
        total = total + item
    return total


tom_total = calculate_total(tom_expense_list)
joe_total = calculate_total(joe_expense_list)
print("......Using a function........")
print("Tom's total expense:", tom_total)
print("Joe's total expense:", joe_total)
