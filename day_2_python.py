#! /usr/local/bin/python

import pandas as pd

# Load a CSV file
alz_df = pd.read_csv('Alzheimer_s_Disease_and_Healthy_Aging_Data.csv')

# Display the first 5 rows
print(alz_df.head())
