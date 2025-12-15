import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_FILE = "data/processed/books_clean.csv"
OUTPUT_DIR = "results/"

def main():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Cleaned dataset not found: {DATA_FILE}")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    df = pd.read_csv(DATA_FILE)
    print("Loaded:", len(df), "rows")

    # 1. Price Distribution Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df["price"], bins=10, edgecolor="black")
    plt.title("Price Distribution of Books")
    plt.xlabel("Price (£)")
    plt.ylabel("Count")
    plt.savefig(os.path.join(OUTPUT_DIR, "price_distribution.png"))
    plt.close()

    # 2. Rating Distribution Bar Chart
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["rating"])
    plt.title("Rating Distribution")
    plt.xlabel("Star Rating")
    plt.ylabel("Count")
    plt.savefig(os.path.join(OUTPUT_DIR, "rating_distribution.png"))
    plt.close()

    # 3. Price vs Rating Boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="rating", y="price", data=df)
    plt.title("Price vs Rating")
    plt.savefig(os.path.join(OUTPUT_DIR, "price_vs_rating.png"))
    plt.close()

    # 4. Top 10 Expensive Books
    top10 = df.nlargest(10, "price")
    plt.figure(figsize=(12, 6))
    sns.barplot(x="price", y="title", data=top10)
    plt.title("Top 10 Most Expensive Books")
    plt.xlabel("Price (£)")
    plt.ylabel("Book Title")
    plt.savefig(os.path.join(OUTPUT_DIR, "top10_expensive_books.png"))
    plt.close()

    print("All plots saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
