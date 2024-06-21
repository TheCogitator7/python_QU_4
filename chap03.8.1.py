import seaborn as sns
import numpy as np
import pandas as pd


df=sns.load_dataset('mpg')
print(df.head())

df['ratio']=(df['mpg'] / df['weight'])*100
print(df.head())


num=pd.Series([-2, -1, 1, 2])
print(np.where(num >= 0))

print(np.where(num >= 0, '양수', '음수'))


df['horse_power_div']=np.where(df['horsepower'] < 100, '100 미만',
                               np.where((df['horsepower'] >= 100) & (df['horsepower'] < 200), '100 이상',
                                        np.where(df['horsepower'] >= 200, '200 이상', '기타')))

print(df.head(8))
