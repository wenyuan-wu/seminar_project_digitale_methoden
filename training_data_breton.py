import pandas as pd
from sklearn.model_selection import train_test_split

col_names = ["hist", "norm"]
df = pd.read_csv("data/breton_raw.tsv", sep="\t", names=col_names)

train, test = train_test_split(df, test_size=0.2, random_state=1633)
dev = test

print(len(train))
print(len(test))
print(len(dev))

train.to_csv("data/breton_train.tsv", sep="\t", header=False, index=False)
test.to_csv("data/breton_test.tsv", sep="\t", header=False, index=False)
dev.to_csv("data/breton_dev.tsv", sep="\t", header=False, index=False)
