import pandas as pd
from pandas import DataFrame

period = 20

df = pd.read_csv('AUDNZD1440.csv')
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

df[str(period) + '-period CMF'].to_csv(
    r'C:\PythonProjects\Forex\cmfAUDNZD1440.csv', header=True)

# Does NOT reflect OANDA results. Already checked formula accuracy.
