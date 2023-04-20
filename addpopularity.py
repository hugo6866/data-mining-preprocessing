import pandas as pd

df = pd.read_csv("resto_cleaned.csv", delimiter=';')

# Low popularity: Rating < 3.5 and Rating Count < 100
# Medium popularity: Rating >= 3.5 and Rating < 4.5 or Rating Count >= 100 and Rating Count < 300
# High popularity: Rating >= 4.5 and Rating Count >= 300


def determine_popularity(row):
    if row['Rating'] < 3.5 and row['Rating Count'] < 100:
        return 'Low'
    elif (row['Rating'] >= 3.5 and row['Rating'] < 4.5) or (row['Rating Count'] >= 100 and row['Rating Count'] < 300):
        return 'Medium'
    else:
        return 'High'


df['Popularity'] = df.apply(determine_popularity, axis=1)

df.to_csv("resto_cleaned.csv", index=False, sep=';')
