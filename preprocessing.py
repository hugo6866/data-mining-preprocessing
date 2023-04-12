import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import csv as csv
import pickle

df = pd.read_csv('resto_clean.csv',
                 delimiter=';', header=0)

categories = df['Category'].str.get_dummies(', ')
categories.columns = ['Category_' + col for col in categories.columns]

df = pd.concat([df, categories], axis=1)

df.drop(['Category'], axis=1, inplace=True)

subdistrict_le = LabelEncoder()
df['subdistrict'] = subdistrict_le.fit_transform(df['subdistrict'])
district_le = LabelEncoder()
df['District'] = district_le.fit_transform(df['District'])

with open('subdistrict_encoder.pickle', 'wb') as f:
    pickle.dump(subdistrict_le, f)

with open('district_encoder.pickle', 'wb') as f:
    pickle.dump(district_le, f)

df.to_csv('resto_preprocessed.csv', index=False, sep=";",
          encoding='utf-8', quoting=csv.QUOTE_NONNUMERIC)

print(df.head())
