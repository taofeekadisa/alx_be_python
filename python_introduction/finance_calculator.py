monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_saving = float(monthly_income)  - float(monthly_expenses)

print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${int(monthly_saving * 12 + (monthly_saving * 12 * 0.05))}.")