# backend/models.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./finance.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id          = Column(Integer, primary_key=True, index=True)
    date        = Column(Date)
    description = Column(String)
    amount      = Column(Float)
    category    = Column(String, default="Uncategorized")

def init_db():
    Base.metadata.create_all(bind=engine)