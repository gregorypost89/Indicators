import pandas as pd
from pandas import DataFrame

# Part 1: Rate of Change Calculation

######################
# Input Period Below:#
######################
period = 5
#####################

df = pd.read_csv('data/ATR.csv', usecols=['date', 'close', 'ATR', 'pipGain'])

df['pastPrice'] = df['close'].shift(periods=period)

df['roc'] = ((df['close'] - df['pastPrice']) / df['pastPrice']) * 100

df['shift'] = df['roc'].shift(periods=1)

rocIsPositive = []
shiftIsPositive = []

for x in df['roc']:
    if x > 0:
        rocIsPositive.append(True)
    else:
        rocIsPositive.append(False)

for y in df['shift']:
    if y > 0:
        shiftIsPositive.append(True)
    else:
        shiftIsPositive.append(False)

idList = [0]

identifier = 1
for z in range(0, len(rocIsPositive)):
    if rocIsPositive[z] != shiftIsPositive[z]:
        idList.append(identifier)
        identifier += 1
    else:
        idList.append(identifier)

df['id'] = pd.DataFrame(idList)

df = df.drop(df.index[0:period])

# print(rocIsPositive)
# print(len(rocIsPositive))
# print(shiftIsPositive)
# print(len(shiftIsPositive))
# print(finalList)

# zipList = list(zip(dateList, closeList, atrList, rocList, shortId, longId))
# df2 = DataFrame(zipList, columns=['date', 'close', 'ATR', 'rateOfChange(5)',
#                                   'shortID', 'longID'])
# df2.to_csv(r'C:\GithubProjects\Indicators\output\ROC.csv')

df.to_csv(r'C:\GithubProjects\Indicators\output\test.csv',
          columns=['date', 'close', 'ATR', 'roc', 'pipGain', 'id'])
