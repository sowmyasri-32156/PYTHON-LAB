import pandas as pd
df_csv=pd.read_csv('sample.csv')
print("data frames from csv:",df_csv)
df_json=pd.read_json('sample.json')
print("data frame from json:",df_json)