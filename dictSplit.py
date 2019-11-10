import pandas as pd
df = pd.read_csv('C:/users/grego/desktop/test1.csv', usecols=['identifier', 'dailyPips'])
total = df.groupby(['identifier']).sum()
print(total)
