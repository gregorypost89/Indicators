import pandas as pd
from pandas import DataFrame

df = pd.read_csv('AUDNZD1440.csv')
df = DataFrame(df, columns=['Date', 'Close'])

smaPeriod = 30
df['SMA' + str(smaPeriod)] = df['Close'].rolling(window=smaPeriod).mean()

#This is to calculate a range of Simple Moving Averages:

# x = 3
# while x < 31:
#     newDf['SMA' + str(x)] = newDf['Close'].rolling(window=x).mean()
#     x += 1
# newDf.to_csv(r'C:\PythonProjects\Forex\newAUDNZD1440.csv')
