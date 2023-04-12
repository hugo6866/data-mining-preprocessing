import pandas as pd
import csv as csv
df = pd.read_csv('resto_clean.csv', delimiter=';', header=0)

categories = df['Category'].str.get_dummies(', ')
categories.columns = ['Category_' + col for col in categories.columns]

df = pd.concat([df, categories], axis=1)

df.drop(['Category'], axis=1, inplace=True)


df.to_csv('restogg_updated_cleaned_onehot.csv',
          index=False, sep=";", encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)
