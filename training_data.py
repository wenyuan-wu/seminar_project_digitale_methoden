import pandas as pd
from sklearn.model_selection import train_test_split

col_names = ["hist", "norm", "year"]
df = pd.read_csv("data/breton_devri.csv", sep=",", names=col_names)

df_raw = df[df["year"].between(1900, 2000)]
df_raw = df_raw.drop(columns=["year"])
print(len(df_raw))

train, test = train_test_split(df_raw, test_size=0.2)
print(len(train))
print(len(test))

df_raw.to_csv("data/period_7_raw.csv", sep="\t", header=False, index=False)
train.to_csv("data/period_7_train.csv", sep="\t", header=False, index=False)
test.to_csv("data/period_7_test.csv", sep="\t", header=False, index=False)
