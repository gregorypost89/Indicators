import pandas as pd
import random

# Create data for USD
random.seed(1)
# print(random.sample(range(1, 30), 10))

usdVals = {'value': [10, 11, 11, 12, 18, 16, 14, 10, 11, 13]}

# Create dataframe for USD
dfusd = pd.DataFrame(usdVals)

# Show
#print(dfusd)

# Calculate the moving average, where x in window=x is the number of
# periods calculated

sma2pd = (dfusd.rolling(window=2).mean())

dftoList = sma2pd.values.tolist()
smaList = [val for sublist in dftoList for val in sublist]  # Strip brackets

print(smaList)
