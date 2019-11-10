import pandas as pd
from pandas import DataFrame

# Part 1: Rate of Change Calculation

######################
# Input Period Below:#
######################
period = 5
#####################

df = pd.read_csv('data/AUDNZD1440.csv', usecols=['date', 'close'])

xDaysAgoPrice = df.close.shift(periods=period)

dateList = df.date.tolist()
closeList = df.close.tolist()
xDayAgoList = xDaysAgoPrice.tolist()

rocList = []

for x in closeList:
    for y in xDayAgoList:
        rocList.append(((x-y)/y) * 100)

# Part 2: Identifier
# Identify the area where we enter

# Section 1: Short Positions

shortId, longId = [], []
for p in range(0, (period + 1)):
    shortId.append(0), longId.append(0)

shortIdentifier = 1
for x in rocList:
    if x < 0:
        shortId.append(shortIdentifier)
    elif x > 0:
        shortId.append(0)
        shortIdentifier += 1

longIdentifier = 1
for y in rocList:
    if y > 0:
        longId.append(longIdentifier)
    elif y < 0:
        longId.append(0)
        longIdentifier += 1


zipList = list(zip(dateList, closeList, rocList, idList))
df2 = DataFrame(zipList, columns=['date', 'close', 'rateOfChange(5)', 'id'])
df2.to_csv(r'C:\GithubProjects\Indicators\output\ROC.csv')

# Section 2: Long Positions

