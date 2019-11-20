# --------------------------------------------
# |              dataManipulaion.py          |
# --------------------------------------------
#
# The purpose of this program is to transform excel data extracted from MT4.
# We can repurpose sections of this code into individual .py files for organization and utility.

# Task 1: Two-line cross confirmation indicator - Pips gained

# Description - We need to sum up the pips gained during the period where we went short and stop
# when we go long, and vice versa

# TODO: Determine how to identify the areas that need to be summed.
# TODO: 1) We identify where indShort > indLong
# TODO: a) This is columns B and C
# TODO: b) We take the value of close (column A) and sum those values together where the condition=True
# TODO: c) use Numpy to return arrays for the columns

import pandas as pd

df1 = pd.read_csv('C:/users/grego/desktop/test.csv', usecols=[1], encoding='utf-8')
df2 = pd.read_csv('C:/users/grego/desktop/test.csv', usecols=[2], encoding='utf-8')
a = df1.to_numpy()
b = df2.to_numpy()
short = a.tolist()
long = b.tolist()
print(short)
print(long)

x = 0
while x < 9:
    sValue = short[x]
    lValue = long[x]
    if sValue < lValue:
        print("True")
    else:
        print("False")
    x += 1

# Result: [1, 1, 1, 0, 0, 0, 4, 4, 4]
# This identifies each true section individually and all false sections
# TODO: For future, try to see if we can increment in series (0, 1, 2)

s = pd.Series(id)
s.to_csv('C:/users/grego/desktop/test1.csv', 'columns=2')
# Remember to always save to a new file for now, so we don't overwrite our
# original data
# TODO: Return identifier as a separate workbook

import pandas as pd
df = pd.read_csv('C:/users/grego/desktop/test1.csv', usecols=['identifier', 'dailyPips'])
total = df.groupby(['identifier']).sum()
print(total)

#             dailyPips
# identifier
# 0.0           0.23975
# 4.0          -0.07711
# 13.0         -0.01807
# 32.0         -0.01897
# 42.0         -0.05027
# 43.0         -0.00648
# 60.0         -0.00641
# 73.0         -0.00067
# 80.0         -0.01685
# 99.0         -0.10709
# 100.0        -0.05642

# This is consistent with the excel spreadsheet data