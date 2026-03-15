## Parser for bank csv files
import pandas as pd

BANK_FORMATS = {
    "wells": {"date": "Date", "amount": "Amount", "desc": "Description"},
    "bofa": {"date": "Date", "amount": "Amount", "desc": "Description"},
    "discover": {"date": "Date", "amount": "Amount", "desc": "Description"},
}

##Parser
## filepath = file path of bank statement(csv) 
## bank = bank name from BANK_FORMATS
def parse_csv(filepath: str, bank: str) -> list[dict]:
    fmt = BANK_FORMATS.get(bank)
    df = pd.read_csv(filepath)
    df = df.rename(columns={
        fmt["date"]: "date",
        fmt["amount"]: "amount",
        fmt["desc"]: "description"
    })
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    return df[["date", "amount", "description"]].to_dict(orient="records")