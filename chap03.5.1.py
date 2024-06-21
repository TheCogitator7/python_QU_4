import seaborn as sns

df=sns.load_dataset('titanic')
print(df.head())

print(df.info())

print(df.head().isnull())

df.dropna()

df.dropna(subset=['age'], axis=0)

df.dropna(axis=1)

df.dropna(axis=1, thresh=300)
