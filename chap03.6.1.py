import seaborn as sns

df=sns.load_dataset('mpg')
print(df.head())

df.set_index('name', inplace=True)
print(df.head())

df.sort_index(inplace=True)
print(df.head())

df.sort_index(inplace=True, ascending=False)
print(df.head())

df.reset_index(inplace=True)
print(df.head())



