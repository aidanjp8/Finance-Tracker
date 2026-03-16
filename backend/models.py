# backend/models.py
"""
Database models and configuration for the Personal Finance Tracker.
Uses SQLAlchemy ORM with a local SQLite database.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# Path to the SQLite database file — stored locally in the backend folder
DATABASE_URL = "sqlite:///./finance.db"

# Engine: the core connection to the database
# check_same_thread=False allows FastAPI to access it across multiple requests
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal: factory for creating database sessions
# Each request to the API will open and close its own session
SessionLocal = sessionmaker(bind=engine)

# Base: parent class for all database models
# SQLAlchemy uses this to track and register tables
Base = declarative_base()


class Transaction(Base):
    """
    Represents a single financial transaction.
    Maps to the 'transactions' table in the database.

    Attributes:
        id          (int):   Auto-incrementing unique identifier
        date        (date):  Date the transaction occurred
        description (str):   Raw description from the bank CSV
        amount      (float): Transaction amount (negative = expense, positive = income)
        category    (str):   Spending category, defaults to 'Uncategorized'
    """

    __tablename__ = "transactions"

    id          = Column(Integer, primary_key=True, index=True)
    date        = Column(Date)
    description = Column(String)
    amount      = Column(Float)
    category    = Column(String, default="Uncategorized")


def init_db():
    """
    Initializes the database by creating all tables defined in Base.
    Safe to call multiple times — only creates tables that don't exist yet.
    Called once at application startup in main.py.
    """
    Base.metadata.create_all(bind=engine)