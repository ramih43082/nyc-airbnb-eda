import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    # 1. Setup Environment
    # Create an images folder to store the output charts
    os.makedirs('images', exist_ok=True)

    print("Loading data...")
    # Load dataset (ensure your terminal is in the project root directory)
    df = pd.read_csv('data/new_york_listings_2024.csv')
    print(f"Original dataset shape: {df.shape}")

    # 2. Data Cleaning
    print("Cleaning data...")
    # Filter: Keep realistic prices to remove 'joke' listings and $0 placeholders
    df_clean = df[(df['price'] > 0) & (df['price'] < 1000)].copy()
    
    rows_removed = len(df) - len(df_clean)
    print(f"Removed {rows_removed} outlier listings.")
    print(f"Cleaned dataset shape: {df_clean.shape}")

    # 3. Generating Visualizations
    print("Generating visualizations...")

    # Chart 1: Price Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df_clean['price'], bins=50, kde=True, color='teal')
    plt.title("Price Distribution (Listings < $1000)")
    plt.xlabel("Price per Night ($)")
    plt.ylabel("Count")
    plt.tight_layout() # Ensures labels don't get cut off
    plt.savefig('images/01_price_distribution.png')
    plt.close() # Closes the figure from memory

    # Chart 2: Average Price by Borough & Room Type
    plt.figure(figsize=(14, 7))
    sns.barplot(
        data=df_clean, 
        x='neighbourhood_group', 
        y='price', 
        hue='room_type', 
        palette='viridis'
    )
    plt.title("Average Price by Borough & Room Type (NYC 2024)")
    plt.ylabel("Average Price ($)")
    plt.xlabel("Borough")
    plt.legend(title="Room Type", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('images/02_avg_price_by_borough_roomtype.png')
    plt.close()

    # Chart 3: Supply Density (Heatmap)
    price_matrix = pd.crosstab(df_clean['neighbourhood_group'], df_clean['room_type'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(price_matrix, annot=True, fmt='d', cmap='YlGnBu')
    plt.title("Number of Listings: Borough vs. Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Borough")
    plt.tight_layout()
    plt.savefig('images/03_supply_heatmap.png')
    plt.close()

    # Chart 4: Geospatial Distribution
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=df_clean, 
        x='longitude', 
        y='latitude', 
        hue='neighbourhood_group', 
        s=10, 
        alpha=0.5
    )
    plt.title("Geographic Distribution of NYC Listings (2024)")
    plt.legend(title="Borough")
    plt.tight_layout()
    plt.savefig('images/04_geospatial_map.png')
    plt.close()

    print("EDA complete! All charts have been saved to the 'images/' folder.")

if __name__ == "__main__":
    main()