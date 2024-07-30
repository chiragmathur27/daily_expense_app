from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum

class User(BaseModel):
    email: EmailStr
    name: str
    mobile: str

class SplitMethod(str, Enum):
    EQUAL = "equal"
    EXACT = "exact"
    PERCENTAGE = "percentage"

class ExpenseSplit(BaseModel):
    user_email: EmailStr
    amount: float

class Expense(BaseModel):
    payer_email: EmailStr
    amount: float
    description: str
    split_method: SplitMethod
    splits: List[ExpenseSplit]

class BalanceSheet(BaseModel):
    user_email: EmailStr
    balance: float