# Budget App

A category-based budgeting tool that tracks deposits, withdrawals, and
transfers across multiple spending categories, with a visual breakdown
of spending by category.

## Features
- Category class with deposit, withdraw, and transfer functionality
- Automatic funds-checking to prevent overdrawing a category
- Formatted ledger printout showing transaction history and running balance
- ASCII bar chart (`create_spend_chart`) visualizing percentage spent
  per category

## Example
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
print(food)
```

Output includes a formatted ledger and a spend chart like:
Percentage spent by category
100|
90|
80|
70|
60| o
50| o
40| o o
30| o o o
20| o o o
10| o o o
0| o o o
----------
F C A
o l u
o t
d o
