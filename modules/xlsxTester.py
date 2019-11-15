# NOTE: This file is for testing xlsx files that have been created in
# resultsTracker.py.  This is so we do not have to create a new xlsx object
# every time, or comment and uncomment various lines of code

import pandas as pd

data = pd.read_excel(r'C:\GithubProjects\Indicators\output\xlsxtester.xlsx',
                     sheet_name=None, index_col=None, header=None)

for i in range (0, len(data) - 1):
