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