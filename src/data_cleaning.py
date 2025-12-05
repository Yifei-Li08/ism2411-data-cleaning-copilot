# The purpose of this script is to load CSV data, clean and preprocess it,
# and practice using GitHub Copilot to generate and refine functions.

import pandas as pd
import numpy as np

# Load the raw sales data from a CSV file
def load_data(file_path: str):
    return pd.read_csv(file_path)

# Standardize column names to lowercase and replace spaces with underscores
# Because consistent column names look better and are easier to work with
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


# Function generated with GitHub Copilot and slightly modified
# AI uses the wrong column name ‘product_name’ instead of 'prodname'
# Strip leading/trailing whitespace from product names and categories
# Because whitespace can cause issues with grouping and analysis
def clean_product_info(df):
    df['prodname'] = df['prodname'].str.strip()
    df['category'] = df['category'].str.strip()
    return df

# Function generated with GitHub Copilot and slightly modified
# AI uses the wrong column name ‘quantity’ instead of 'qty'
# AI did not realize that the missing values are represented as empty strings or spaces
# Handle missing prices, quantities, and dates_sold (drop rows with missing values)
# Because missing values are dangerous for analysis and should be removed

def handle_missing_values(df):
    df = df.replace(r'^\s*$', np.nan, regex=True)  # Replace empty strings with NaN
    df = df.dropna(subset=['price', 'qty', 'date_sold'])
    return df

# Remove rows with clearly invalid values (negative quantity, negative price)
# Because negative values for price or quantity are not realistic in sales data
def remove_invalid_rows(df):
    df['price'] = df['price'].astype(float)
    df['qty'] = df['qty'].astype(float)
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]
    return df