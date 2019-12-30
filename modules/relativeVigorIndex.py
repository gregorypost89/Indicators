import pandas as pd

# Relative vigor index

# Definitions

# a = close - open
# b = close - open (1 day prior)
# c = close - open (2 days prior)
# d = close - open (3 days prior)
# e = high - low
# f = high - low (1 day prior)
# g = high - low (2 days prior)
# h = high - low (3 days prior)

# Conversions:

## Formulas

# Numerator:
df = pd.read_csv('C:\\GithubProjects\\Indicators\\modules\\AUDNZD1440.csv', usecols=['date', 'open', 'high', 'low', 'close'])
period = 20

df['rvi_a'] = df['close'] - df['open']
df['rvi_b'] = df['close'].shift(periods=1) - df['open'].shift(periods=1)
df['rvi_c'] = df['close'].shift(periods=2) - df['open'].shift(periods=2)
df['rvi_d'] = df['close'].shift(periods=3) - df['open'].shift(periods=3)
df['rvi_e'] = df['high'] - df['low']
df['rvi_f'] = df['high'].shift(periods=1) - df['low'].shift(periods=1)
df['rvi_g'] = df['high'].shift(periods=2) - df['low'].shift(periods=2)
df['rvi_h'] = df['high'].shift(periods=3) - df['low'].shift(periods=3)

df['numerator'] = (df['rvi_a'] + (2 * df['rvi_b']) + (2 * df['rvi_c']) + df[
    'rvi_d']) / 6
df['denominator'] = (df['rvi_e'] + (2 * df['rvi_f']) + (2 * df['rvi_g']) + df[
    'rvi_h']) / 6

df['numerator_rolling'] = df['numerator'].rolling(period).mean()
df['denominator_rolling'] = df['denominator'].rolling(period).mean()
numList = []
denomList = []
for x in df['numerator_rolling']:
    numList.append(x)
for y in df['denominator_rolling']:
    denomList.append(y)
resultList = [x/y for x, y in zip(numList, denomList)]
df['rvi'] = pd.DataFrame(resultList)
print(df)
df['rvi_i'] = df['rvi'].shift(periods=1)
df['rvi_j'] = df['rvi'].shift(periods=2)
df['rvi_k'] = df['rvi'].shift(periods=3)
df['signal_line'] = (df['rvi'] + (2 * df['rvi_i']) + (2 * df['rvi_j']) + df[
    'rvi_k']) / 6
df['signal_line_a'] = df['signal_line'].shift(periods=1)

df['exit'] = df['rvi'].apply(lambda z: 'Exit' if (df['rvi_i'] - df[
    'signal_line_a'] < 0 and df['rvi'] - df['signal_line'] > 0) or (
                                                             df['rvi_i'] - df[
                                                         'signal_line_a'] > 0 and
                                                             df['rvi'] - df[
                                                                 'signal_line'] < 0) else '')


def relative_vigor_index(df, period):
    df['rvi_a'] = df['close'] - df['open']
    df['rvi_b'] = df['close'].shift(periods=1) - df['open'].shift(periods=1)
    df['rvi_c'] = df['close'].shift(periods=2) - df['open'].shift(periods=2)
    df['rvi_d'] = df['close'].shift(periods=3) - df['open'].shift(periods=3)
    df['rvi_e'] = df['high'] - df['low']
    df['rvi_f'] = df['high'].shift(periods=1) - df['low'].shift(periods=1)
    df['rvi_g'] = df['high'].shift(periods=2) - df['low'].shift(periods=2)
    df['rvi_h'] = df['high'].shift(periods=3) - df['low'].shift(periods=3)

    df['numerator'] = (df['rvi_a'] + (2 * df['rvi_b']) + (2 * df['rvi_c']) + df['rvi_d'])/6
    df['denominator'] = (df['rvi_e'] + (2 * df['rvi_f']) + (2 * df['rvi_g']) + df['rvi_h'])/6

    df['numerator_rolling'] = df['numerator'].rolling(period).mean()
    numList = []
    for x in df['numerator_rolling']:
        x = df['numerator_rolling']
        numList.append(x)
    df['denominator_rolling'] = df['denominator'].rolling(period).mean()
    denomList = []
    for y in df['numerator_rolling']:
        y = df['numerator_rolling']
        denomList.append(x)
    print(numList)
    print(denomList)
    # df['rvi'] = df['numerator_rolling']/df['denominator_rolling']
    # df['rvi_i'] = df['rvi'].shift(periods=1)
    # df['rvi_j'] = df['rvi'].shift(periods=2)
    # df['rvi_k'] = df['rvi'].shift(periods=3)
    # df['signal_line'] = (df['rvi'] + (2 * df['rvi_i']) + (2 * df['rvi_j']) + df['rvi_k'])/6
    # df['signal_line_a'] = df['signal_line'].shift(periods=1)
    #
    # df['exit'] = df['rvi'].apply(lambda x: 'Exit' if (df['rvi_i'] - df['signal_line_a'] < 0 and df['rvi'] - df['signal_line'] > 0) or (df['rvi_i'] - df['signal_line_a'] > 0 and df['rvi'] - df['signal_line'] < 0) else '')

#rvi yellow
#signal red
# two lines cross



