import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import csv as csv
import pickle

df = pd.read_csv('resto_clean_full.csv',
                 delimiter=';', header=0)

df.drop(['ID', 'Name', 'Location', 'Address', 'Delivery', 'Rating Count',
        'Highest Price Name', 'Lowest Price Name', 'Rating'], axis=1, inplace=True)

df.to_csv('resto_cleaned.csv', index=False, sep=";",
          encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)

print(df.head())
