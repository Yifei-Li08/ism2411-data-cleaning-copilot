# ISM2411 Data Cleaning Project

## Overview
This project cleans raw sales data using Python and GitHub Copilot. The goal is to make the data ready for analysis.

## What the script does
- Standardizes column names (lowercase, underscores, trimmed spaces)
- Strips whitespace from product names and categories
- Handles missing values (empty strings or spaces converted to NaN, then dropped)
- Removes rows with negative price or quantity
- Saves the cleaned data to `data/processed/sales_data_clean.csv`

## File Structure
ism2411-data-cleaning-copilot/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv
│   └── processed/
│       └── sales_data_clean.csv        # created by your script
├── src/
│   └── data_cleaning.py                # your main script
├── README.md                           # short project description
└── reflection.md                       # your written explanation

## How to Run
1. Make sure Python, pandas, and numpy are installed.
2. Run the script from the project root:
   ```bash
   python src/data_cleaning.py
   ```
The cleaned data will be saved in data/processed/.
The terminal will show a preview of the cleaned dataset.