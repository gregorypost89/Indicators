import pandas as pd
from pandas import DataFrame
import openpyxl

# Part 1: Rate of Change Calculation

####################################
# Input Period and ATR Range Below:#
####################################
period = 5
ATR = 14
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

idList = []

identifier = 1
for z in range(0, len(rocIsPositive)):
    if rocIsPositive[z] != shiftIsPositive[z]:
        idList.append(identifier)
        identifier += 1
    else:
        idList.append(identifier)

df['id'] = DataFrame(idList)

df = df.drop(df.index[0:(ATR-1)])

print(rocIsPositive)
print(len(rocIsPositive))
print(shiftIsPositive)
print(len(shiftIsPositive))


# zipList = list(zip(dateList, closeList, atrList, rocList, shortId, longId))
# df2 = DataFrame(zipList, columns=['date', 'close', 'ATR', 'rateOfChange(5)',
#                                   'shortID', 'longID'])
# df2.to_csv(r'C:\GithubProjects\Indicators\output\ROC.csv')

df.to_csv(r'C:\GithubProjects\Indicators\output\test.csv',
          columns=['date', 'close', 'ATR', 'pipGain', 'roc', 'id'])
#
#
# def UseOpenpyxl(file_name):
#     wb = openpyxl.load_workbook(file_name, read_only=True)
#     sheet = wb.active
#     rows = sheet.rows
#     first_row = [cell.value for cell in next(rows)]
#     data = []
#     for row in rows:
#         record = {}
#         for key, cell in zip(first_row, row):
#             if cell.data_type == 's':
#                 record[key] = cell.value.strip()
#             else:
#                 record[key] = cell.value
#         data.append(record)
#     return data
#
# openpyxlResults = UseOpenpyxl('')
