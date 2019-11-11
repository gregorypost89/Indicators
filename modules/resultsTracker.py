import pandas as pd
from pandas import DataFrame

df = pd.read_csv(r'C:\GithubProjects\Indicators\output\test.csv',
                 usecols=['date', 'close', 'ATR', 'roc', 'pipGain', 'id'])

entries = int(df['id'].iloc[-1])

for i in range(0, entries):
    df2 = df.loc[df['id'] > i]

df.append(df2)

df2.to_csv(r'C:\GithubProjects\Indicators\output\test2.csv')