import pandas as pd
from pandas import ExcelWriter

###################################################
# Define the maximum amount of entries to inspect #
maxEntries = 30

# Put the path of the data file below. Do not replace r or quotes ''. #
inputPath = r'C:\GithubProjects\Indicators\output\test.csv'

# Put the path of the data file below. Do not replace r or quotes ''. #
outputPath = r'C:\GithubProjects\Indicators\output\test4.xlsx'
###################################################

df = pd.read_csv(inputPath,
                 usecols=['date', 'close', 'ATR', 'roc', 'pipGain', 'id'],
                 index_col=None)

maxId = df['id'].loc[len(df['id']) - 1]

if maxId - maxEntries < 0:
    maxEntries = maxId

dataList = []

for i in range((maxId - maxEntries), maxId):
    dfNew = df.where(df['id'] >= i)
    dataList.append(dfNew)


def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, dfl in enumerate(list_dfs, 1):
            dfl.dropna(axis=0, how='all').to_excel(writer, 'sheet%s' % n)
        writer.save()


save_xls(dataList, outputPath)

#C:\GithubProjects\Indicators\output\test.csv