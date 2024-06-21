import seaborn as sns
df=sns.load_dataset('mpg')

print(df.tail(10))

print(df['cylinders'].unique())

filter_bool=(df['cylinders']==4)
print(filter_bool.tail(10))

df.loc[filter_bool, ]

filter_bool_2=(df['cylinders'] == 4) & (df['horsepower'] >= 100)
df.loc[filter_bool_2, ['cylinders', 'horsepower', 'name']]
