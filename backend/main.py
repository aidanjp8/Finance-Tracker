# Run with:
    #fastapi dev main.py

from fastapi import FastAPI, UploadFile, File
from models import init_db, SessionLocal, Transaction
from parser import parse_csv
from categorizer import categorize
import shutil
import os

app = FastAPI()

init_db()


@app.get("/")
def root():
    return {"status": "Finance Tracker API is running"}

# Upload new statement 
@app.post("/upload")
def upload_csv(file: UploadFile = File(...), bank: str = "wells"):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transactions = parse_csv(temp_path, bank)

    db = SessionLocal()
    for t in transactions:
        transaction = Transaction(
            date=t["date"],
            amount=t["amount"],
            description=t["description"],
            category=categorize(t["description"])
        )
        db.add(transaction)

    db.commit()
    db.close()
    os.remove(temp_path)

    return {"message": f"{len(transactions)} transactions imported"}

# Get all transactions
@app.get("/transactions")
def get_transactions():
    db = SessionLocal()
    transactions = db.query(Transaction).all()
    db.close()

    return [
        {
            "id": t.id,
            "date": str(t.date),
            "description": t.description,
            "amount": t.amount,
            "category": t.category
        }
        for t in transactions
    ]

# Spending by category
@app.get("/summary")
def get_summary():
    db = SessionLocal()
    transactions = db.query(Transaction).all()

    summary = {}
    for t in transactions:
        if t.category not in summary:
            summary[t.category] = 0
        summary[t.category] += t.amount

    db.close()

    return {category: round(total, 2) for category, total in summary.items()}

# Update category id(int) to str
@app.patch("/transactions/{transaction_id}")
def update_category(transaction_id: int, category: str):
    db = SessionLocal()
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        db.close()
        return {"error": "Transaction not found"}

    transaction.category = category
    db.commit()
    db.close()

    return {"message": "Category updated", "id": transaction_id, "category": category}

# Clear all data
@app.delete("/transactions")
def clear_transactions():
    db = SessionLocal()
    deleted = db.query(Transaction).delete()
    db.commit()
    db.close()

    return {"message": f"{deleted} transactions deleted"}