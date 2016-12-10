from pandas.io.parsers import read_csv

df = read_csv("WHO_first9cols.csv")

print(df)
print(df.shape)
print(len(df))
print(df.columns)
print(df.dtypes)
print(df.index)
print(df.values)