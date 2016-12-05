import numpy as np
import pandas as pd
import visuals as vs
import matplotlib as plt

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

print(full_data.head())