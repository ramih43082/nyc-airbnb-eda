# NYC Airbnb 2024 Exploratory Data Analysis

## Overview
This repository contains an Exploratory Data Analysis (EDA) of the 2024 New York City Airbnb dataset sourced from Kaggle. The analysis focuses on data validation, outlier handling, pricing distribution, and geospatial supply mapping across the five boroughs.

## Project Structure
- `Lab Notebook.ipynb`: Initial data profiling, integrity checks (null/duplicate validation), and exploratory visualizations.
- `eda_script.py`: Automated Python script for data cleaning and generation of final visualizations.
- `requirements.txt`: Python environment dependencies.
- `images/`: Directory containing exported data visualizations.
  - `01_price_distribution.png`
  - `02_avg_price_by_borough_roomtype.png`
  - `03_supply_heatmap.png`
  - `04_geospatial_map.png`

## Methodology
1. **Data Validation**: Confirmed 0 missing values across the dataset via boolean summation and matrix visualization. Checked for and logged duplicate records.
2. **Data Cleaning**: Identified extreme right-skewed price outliers (maximum value reaching $100,000). Filtered the dataset to include only valid, typical commercial transactions (`price > 0` and `price < 1000`).
3. **Categorical Analysis**: Grouped data by `neighbourhood_group` and `room_type` to calculate average pricing and assess supply density via crosstabulation.
4. **Geospatial Analysis**: Mapped the distribution of listings using raw latitude and longitude coordinates to identify high-density clusters.

## Technical Stack
- **Language**: Python
- **Libraries**: Pandas, Matplotlib, Seaborn, SciPy
- **Environment**: Positron IDE

## Replication
To run this analysis locally:

1. Clone the repository and navigate to the project root.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the source dataset (`new_york_listings_2024.csv`) is located in a `data/` directory.
4. Execute the analysis script:
   ```bash
   python eda_script.py
   ```