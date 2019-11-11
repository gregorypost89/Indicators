import pandas as pd
from pandas import DataFrame

df = pd.read_csv('data\AUDNZD1440.csv', usecols=['date', 'high', 'low',
                                                 'close'])
df['pipGain'] = df['close'] - df['close'].shift(periods=1)
#df = DataFrame(df, columns=['Date', 'High', 'Low', 'Close'])
df['max1'] = df['high'] - df['low']
df['max2'] = abs(df['high'] - df['close'].shift(periods=1))
df['max3'] = abs(df['low'] - df['close'].shift(periods=1))
df['trueRange'] = df[['max1', 'max2', 'max3']].max(axis=1)
df['ATR'] = df['trueRange'].rolling(window=14).mean()

df.to_csv(r'C:\GithubProjects\Indicators\modules\data\ATR.csv', columns=[
    'date', 'high', 'low', 'close', 'pipGain', 'ATR'])
