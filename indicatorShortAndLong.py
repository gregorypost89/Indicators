#
# Short Indicators:
# Baseline: SMA: Close < SMA
# Confirmation 1: CMF: value < 0
#
# Long Indicators:
# Baseline: SMA: Close > SMA
# Confirmation 1: CMF: value > 0

# Short Scenario
# If Close < SMA
# and CMF < 0
# if at any time Close > SMA  : Exit

import pandas as pd
from pandas import DataFrame

df = pd.read_csv('finalAUDNZD1440.csv')
df['BaselineValue'] = df['Close'] - df['SMA30']
baselineValueList = df['BaselineValue'].tolist()
sampleList = [-2, -1, 1, 2, 3]
short = []
for x in baselineValueList:
    if x < 0:
        short.append(1)
    else:
        short.append(0)
# print(baselineValueList)
# print(short)
df = df.append(short)
print(df)