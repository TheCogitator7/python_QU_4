import seaborn as sns

df=sns.load_dataset('mpg')
print(df.head())

filter_bool_3=(df['name'] == 'ford maverick') | (df['name'] == 'ford mustang ii') | (df['name'] == 'chevrolet impala')
print(df.loc[filter_bool_3, ])


filter_isin=df['name'].isin(['ford maverick', 'ford mustang ii', 'chevrolet impala'])
print(df.loc[filter_isin, ])

print(df.loc[filter_isin, ].sort_values('horsepower'))

