# backend/categorizer.py

CATEGORIES = {
    "Food": ["mcdonald", "chipotle", "doordash", "ubereats", "grubhub", "subway", "whole foods"],
    "Transport": ["uber", "lyft", "gas", "shell", "chevron", "parking"],
    "Entertainment": ["spotify", "netflix", "hulu", "steam", "cinema"],
    "Shopping": ["amazon", "walmart", "target", "ebay"],
    "Groceries": ["costco", "safeway", "king", "trader joes"],
    "Utilities": ["xcel", "comcast", "water", "electric", "xfinity"],
    "Rent": ["redpeak", "rentcafe", "rent"],
    "Depts": ["Westerra", "bofa", "discover"],
    "Subscriptions": ["apple", "alltrails"]
}

def categorize(description: str) -> str:
    description = description.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in description:
                return category

    return "Uncategorized"