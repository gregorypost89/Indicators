import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movingAvgData.csv")
sns.barplot(x=df.date, y=df.value, palette="rocket")
sns.lineplot(x=df.date, y=df.sma2)
plt.show()