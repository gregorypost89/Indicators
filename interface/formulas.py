# This file contains all formulas used in interface.py
# ----------------------------
# 1. Baseline
# 2. Confirmation 1
# 3. Confirmation 2
# 4. Volume
# 5. Exit
# ----------------------------
# 1. Baseline
# ----------------------------


def chaikin_money_flow(df, period):
    df['moneyFlowMultiplier'] = ((df['close'] - df['low']) - (df['high'] - df[
        'close'])) / (df['high'] - df['low'])

    df['moneyFlowVolume'] = df['moneyFlowMultiplier'] * df['volume']

    df[str(period) + '-period CMF'] = df['moneyFlowVolume'].rolling(
        window=period).sum() / df['volume'].rolling(window=period).sum()

    df["baseline0cross"] = df[str(period) + '-period CMF']

# ----------------------------
# 2. Confirmation 1
# ----------------------------


def rate_of_change(df, period):
    df['pastPrice'] = df['close'].shift(periods=period)
    df['roc'] = ((df['close'] - df['pastPrice']) / df['pastPrice']) * 100
    df["1conf0cross"] = df['roc']

# ----------------------------
# 5. Exit
# ----------------------------

def relative_vigor_index(df, period):
