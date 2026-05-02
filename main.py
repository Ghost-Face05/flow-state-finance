from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

class Transaction(BaseModel):
    amount: float
    description: str

class Budget(BaseModel):
    category: str
    limit: float

class Report(BaseModel):
    total_income: float
    total_expenses: float

# In-memory database simulation
users_db = {}

@app.post("/register/", response_model=User)
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    users_db[user.username] = user.password
    return user

@app.post("/login/")
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.post("/transactions/")
async def create_transaction(transaction: Transaction, username: str = Depends(login)):
    # Simulate saving transaction logic
    return transaction

@app.get("/budgets/", response_model=List[Budget])
async def get_budgets(username: str = Depends(login)):
    # Simulate budgets retrieval
    return []

@app.post("/budgets/")
async def create_budget(budget: Budget, username: str = Depends(login)):
    # Simulate budget creation logic
    return budget

@app.get("/reports/", response_model=Report)
async def get_report(username: str = Depends(login)):
    # Simulate reports generation logic
    return Report(total_income=0.0, total_expenses=0.0)