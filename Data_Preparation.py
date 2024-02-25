import pandas as pd

# Load the dataset
data = pd.read_csv('/mnt/data/AtlasofSurveillance.csv')

# Selecting relevant columns for analysis
relevant_columns = ['City', 'County', 'State', 'Agency', 'Type of LEA', 'Technology']
data_clean = data[relevant_columns].copy()

# Handling missing values by filling them with 'Unknown'
data_clean.fillna('Unknown', inplace=True)
