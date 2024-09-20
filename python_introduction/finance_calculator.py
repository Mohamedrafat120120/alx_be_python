user_monthly_income = int(input("Enter your monthly income: "))
user_monthly_total_expenses = int(input("Enter your total monthly expenses: "))
monthly_saving = user_monthly_income - user_monthly_total_expenses
print(f"Your monthly savings are ${monthly_saving}.")
projected_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")