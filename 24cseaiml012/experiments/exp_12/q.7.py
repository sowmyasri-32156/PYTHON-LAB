import pandas as pd
data={
    'name':['alice','bob','charlie'],
    'age':[25,30,35],
    'city':['new york','san francisco','los angeles']
}
df =pd.DataFrame(data)
print("data frame:",df)
print("/n age column:",df['age'])
print("/n row at index1:",df.iloc[1])