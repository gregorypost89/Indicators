import pandas as pd
from pandas import DataFrame

df = pd.read_csv('AUDNZD1440.csv')
df = DataFrame(df, columns=['Date', 'High', 'Low', 'Close'])
df['max1'] = df['High'] - df['Low']
df['max2'] = abs(df['High'] - df['Close'].shift(periods=1))
df['max3'] = abs(df['Low'] - df['Close'].shift(periods=1))
df['True Range'] = df[['max1', 'max2', 'max3']].max(axis=1)
df['ATR14'] = df['True Range'].rolling(window=14).mean()

