class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total_balance = 0
        for transaction in self.ledger:
            total_balance += transaction["amount"]
        return total_balance

    def transfer(self, amount, destination_category):
        if self.withdraw(amount, f"Transfer to {destination_category.name}"):
            destination_category.deposit(
                amount,
                f"Transfer from {self.name}"
            )
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title_length = len(self.name)
        total_spaces = 30 - title_length

        left_stars = total_spaces // 2
        right_stars = total_spaces - left_stars

        title = "*" * left_stars + self.name + "*" * right_stars

        ledger = []

        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = transaction["amount"]

            ledger.append(
                f"{description:<23}{amount:>7.2f}"
            )

        return f"{title}\n" + "\n".join(ledger) + f"\nTotal: {self.get_balance():.2f}"


def create_spend_chart(categories):
    total_spent = 0

    for category in categories:
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total_spent += abs(transaction["amount"])

    category_spending = []

    for category in categories:
        spent = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent += abs(transaction["amount"])

        category_spending.append(spent)

    percentages = []

    for spending in category_spending:
        percentage = int((spending / total_spent) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)


    chart = ["Percentage spent by category"]


    for level in range(100, -1, -10):
        row = f"{level:3}|"

        for percentage in percentages:
            if percentage >= level:
                row += " o "
            else:
                row += "   "
        row+= " "
        chart.append(row)


    chart.append("    " + "-" * (len(categories) * 3 + 1))


    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        row = "     "

        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        

        chart.append(row)


    return "\n".join(chart)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
food.withdraw(100, "restaurant")

clothing = Category("Clothing")
clothing.deposit(500, "initial deposit")
clothing.withdraw(100, "shirt")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(300, "gas")

print(food)
print()
print(clothing)
print()
print(auto)

print(create_spend_chart([food, clothing, auto]))
