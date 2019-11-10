# ATR : averageTrueRange.py (Always Included)
# Baseline : simpleMovingAverage.py
# Confirmation Indicator 1 : chaikinMoneyFlow.py

import pandas as pd
from pandas import DataFrame

atrPeriod = 14
smaPeriod = 30

# ATR

df = pd.read_csv('AUDNZD1440.csv')
df = DataFrame(df, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['max1'] = df['High'] - df['Low']
df['max2'] = abs(df['High'] - df['Close'].shift(periods=1))
df['max3'] = abs(df['Low'] - df['Close'].shift(periods=1))
df['True Range'] = df[['max1', 'max2', 'max3']].max(axis=1)
df['ATR' + str(atrPeriod)] = df['True Range'].rolling(window=14).mean()

# Baseline : simpleMovingAverage.py


df['SMA' + str(smaPeriod)] = df['Close'].rolling(window=smaPeriod).mean()

# Confirmation Indicator 1 : chaikinMoneyFlow.py

period = 20

df['moneyFlowMultiplier'] = ((df['Close'] - df['Low']) - (df['High'] - df[
    'Close'])) / (df['High'] - df['Low'])

# a = df['Close'] - df['Low']
# b = df['High'] - df['Close']
# c = df['High'] - df['Low']
# df['moneyFlow2'] = ((a - b) / c)

# Money Flow Volume = Money Flow Multiplier x Volume for the Period
df['moneyFlowVolume'] = df['moneyFlowMultiplier'] * df['Volume']

# x-period CMF = x-period Sum of Money Flow Volume / x period Sum of Volume
df[str(period) + '-period CMF'] = df['moneyFlowVolume'].rolling(
    window=period).sum() / df['Volume'].rolling(window=period).sum()

# --------------------------------------------------------------------------

# Extract Relevant Columns to csv
df.to_csv(r'C:\PythonProjects\Forex\finalAUDNZD1440.csv',
          columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'ATR' +
                   str(atrPeriod), 'SMA' + str(smaPeriod), str(period) +
                   '-period ''CMF'], header=True)

