import pandas as pd
import os

INPUT_FILE = "data/processed/books_clean.csv"

def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Processed data not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)

    print("\nBasic Info")
    print(df.info())
    
    print("\nSummary Statistics")
    print("Total books:", len(df))
    print("Average price:", round(df["price"].mean(), 2))
    print("Median price:", round(df["price"].median(), 2))
    print("Most expensive price:", df["price"].max())
    print("Cheapest price:", df["price"].min())

    print("\nRating Distribution")
    print(df["rating"].value_counts().sort_index())

    print("\nTop 10 Most Expensive Books")
    top10 = df.nlargest(10, "price")[["title", "price", "rating"]]
    print(top10.to_string(index=False))

    print("\nAnalysis Completed.")

if __name__ == "__main__":
    main()

