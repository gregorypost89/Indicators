import pandas as pd
from pandas import ExcelWriter

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
    dataList.append(dfNew)


def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df1 in enumerate(list_dfs):
            df1.dropna(axis=0, how='all').to_excel(writer, 'sheet%s' % (n+1))
        writer.save()


save_xls(dataList, r'C:\GithubProjects\Indicators\output\test4.xlsx')

C:\GithubProjects\Indicators\output\test.csv