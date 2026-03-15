import pandas as pd

BANK_FORMATS = {
    "wells": {"type": "no_header", "cols": [0, 1, 4], "names": ["date", "amount", "description"]},
    "bofa":  {"type": "header", "date": "Date", "amount": "Amount", "desc": "Description"},
    "discover": {"type": "header", "date": "Trans. Date", "amount": "Amount", "desc": "Description"},
}

def parse_csv(filepath: str, bank: str) -> list[dict]:
    fmt = BANK_FORMATS.get(bank)

    if fmt["type"] == "no_header":
        df = pd.read_csv(filepath, header=None)
        df = df.iloc[:, fmt["cols"]]
        df.columns = fmt["names"]
    else:
        df = pd.read_csv(filepath)
        df = df.rename(columns={
            fmt["date"]: "date",
            fmt["amount"]: "amount",
            fmt["desc"]: "description"
        })

    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])

    return df[["date", "amount", "description"]].to_dict(orient="records")