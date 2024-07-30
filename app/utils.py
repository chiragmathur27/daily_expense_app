from app.models import Expense, SplitMethod
from app.database import database

async def validate_expense(expense: Expense):
    if expense.split_method == SplitMethod.PERCENTAGE:
        total_percentage = sum(split.amount for split in expense.splits)
        if total_percentage != 100:
            raise ValueError("Percentages must add up to 100%")
    elif expense.split_method == SplitMethod.EXACT:
        total_amount = sum(split.amount for split in expense.splits)
        if total_amount != expense.amount:
            raise ValueError("Split amounts must add up to the total expense amount")

async def calculate_balances():
    # Implement balance calculation logic here
    pass