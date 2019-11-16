import pandas as pd

###################################################
# Define the maximum amount of entries to inspect #
maxEntries = 30

# Put the path of the data file below. Do not replace r or quotes ''. #
filePath = r'INSERT FILENAME HERE'
###################################################

df = pd.read_csv(filePath,
                 usecols=['date', 'close', 'ATR', 'roc', 'pipGain', 'id'],
                 index_col=None)

dataList = []

maxId = df['id'].loc[len(df['id']) - 1]

if maxId - maxEntries < 0:
    maxEntries = maxId

for i in range((maxId - maxEntries), maxId):
    dfNew = df.where(df['id'] >= i)
    # Uncomment the following out for unique id names for each column.
    # .rename(columns={'date': 'date' + str(i),
    # 'close': 'close' + str(i), 'ATR': 'ATR' + str(i), 'roc': 'roc' + str(i),
    # 'pipGain': 'pipGain' + str(i), 'id': 'id' + str(i)})
    dataList.append(dfNew)

# Uncomment the following for one sheet in csv format

# print(dataList)
# df4 = pd.concat(dataList, axis=1).dropna(axis=0, how='all')
#
# df4.to_csv(r'C:\GithubProjects\Indicators\output\test3.csv')