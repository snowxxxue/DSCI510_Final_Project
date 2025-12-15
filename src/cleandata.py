import pandas as pd
import re

RAW_FILE = "data/raw/books_5pages.csv"
OUTPUT_FILE = "data/processed/books_clean.csv"

def clean_price(price_str):
    match = re.search(r"[\d.]+", str(price_str))
    return float(match.group()) if match else None

def clean_rating(rating_str):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return rating_map.get(str(rating_str).strip(), None)

def main():
    print("Reading raw file...")

    df = pd.read_csv(RAW_FILE)
    print("Loaded:", df.shape[0], "rows")
    print(df.head())

    print("\nCleaning price column...")
    df["price"] = df["price"].apply(clean_price)

    print("Cleaning rating column...")
    df["rating"] = df["rating"].apply(clean_rating)

    print("\nPreview after cleaning:")
    print(df.head())

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nCleaned data saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()




