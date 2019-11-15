import pandas as pd
from pandas import DataFrame, ExcelWriter
import xlsxwriter

### Define the maximum amount of entries to inspect ###
maxEntries = 30
#######################################################

df = pd.read_csv(r'C:\GithubProjects\Indicators\output\test.csv',
                 usecols=['date', 'close', 'ATR', 'roc', 'pipGain', 'id'],
                 index_col = None)

dataList = []

maxId = df['id'].loc[len(df['id']) - 1]

if maxId - maxEntries < 0:
    maxEntries = maxId

for i in range((maxId - maxEntries), maxId):
    dfnew = df.where(df['id'] >= i)
    #.rename(columns={'date': 'date' + str(i),
    #'close': 'close' + str(i), 'ATR': 'ATR' + str(i), 'roc': 'roc' + str(i),
    #'pipGain': 'pipGain' + str(i), 'id': 'id' + str(i)})
    dataList.append(dfnew)

# Uncomment the following for one sheet in csv format

# print(dataList)
# df4 = pd.concat(dataList, axis=1).dropna(axis=0, how='all')
#
# df4.to_csv(r'C:\GithubProjects\Indicators\output\test3.csv')

# Uncomment the following for separation by sheet in xlsx format:


def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df1 in enumerate(list_dfs):
            df1.dropna(axis=0, how='all').to_excel(writer, 'sheet%s' % n)
        writer.save()


save_xls(dataList, r'C:\GithubProjects\Indicators\output\test4.xlsx')
