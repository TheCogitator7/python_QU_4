import seaborn as sns

df=sns.load_dataset('titanic')

df_2=df.copy()
print(df_2.head(6))

mean_age=df_2['age'].mean()
print(mean_age)

df_2['age'].fillna(mean_age, inplace=True)

print(df_2['age'].head(6))

df_2['embark_town'].fillna('Southampton', inplace=True)

df_2['deck_ffill'] = df_2['deck'].fillna(method='ffill')
df_2['deck_bfill'] = df_2['deck'].fillna(method='bfill')

print(df_2[['deck', 'deck_ffill', 'deck_bfill']].head(12))

