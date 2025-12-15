import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "/Users/shirley/Desktop/510/Final Project/books_clean.csv"

def main():
    df = pd.read_csv(INPUT_FILE)

    # 1. Price Histogram
    plt.figure(figsize=(8,5))
    plt.hist(df["price"], bins=15)
    plt.title("Price Distribution of Books")
    plt.xlabel("Price (£)")
    plt.ylabel("Count")
    plt.grid(alpha=0.3)
    plt.savefig("price_distribution.png")
    plt.close()

    # 2. Rating Bar Chart
    plt.figure(figsize=(8,5))
    df["rating"].value_counts().sort_index().plot(kind="bar")
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.grid(alpha=0.3)
    plt.savefig("rating_distribution.png")
    plt.close()

    # 3. Price vs Rating Scatter Plot
    plt.figure(figsize=(8,5))
    plt.scatter(df["rating"], df["price"], s=40)
    plt.title("Price vs Rating")
    plt.xlabel("Rating")
    plt.ylabel("Price (£)")
    plt.grid(alpha=0.3)
    plt.savefig("price_vs_rating.png")
    plt.close()

    # 4. Top 10 Most Expensive Books
    top10 = df.nlargest(10, "price")

    plt.figure(figsize=(10,6))
    plt.barh(top10["title"], top10["price"])
    plt.title("Top 10 Most Expensive Books")
    plt.xlabel("Price (£)")
    plt.gca().invert_yaxis()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("top10_expensive_books.png")
    plt.close()

    print("\n Visualization Completed!")
    print("Saved files:")
    print("- price_distribution.png")
    print("- rating_distribution.png")
    print("- price_vs_rating.png")
    print("- top10_expensive_books.png")

if __name__ == "__main__":
    main()
