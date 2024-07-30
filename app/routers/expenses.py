from fastapi import APIRouter, HTTPException
from app.models import Expense, BalanceSheet
from app.database import database
from app.utils import calculate_balances, validate_expense
from typing import List

router = APIRouter()

@router.post("/expenses/", response_model=Expense)
async def add_expense(expense: Expense):
    await validate_expense(expense)
    await database.expenses.insert_one(expense.dict())
    await calculate_balances()
    return expense

@router.get("/expenses/{email}", response_model=List[Expense])
async def get_user_expenses(email: str):
    expenses = await database.expenses.find({"payer_email": email}).to_list(None)
    return [Expense(**expense) for expense in expenses]

@router.get("/balances/{email}", response_model=BalanceSheet)
async def get_user_balance(email: str):
    balance = await database.balances.find_one({"user_email": email})
    if not balance:
        raise HTTPException(status_code=404, detail="Balance not found")
    return BalanceSheet(**balance)

@router.get("/balances/download")
async def download_balance_sheet():
    balances = await database.balances.find().to_list(None)
    # Implement balance sheet generation and download logic here
    return {"message": "Balance sheet downloaded"}