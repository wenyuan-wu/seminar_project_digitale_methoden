import pandas as pd
import matplotlib.pyplot as plt

col_names = ["hist", "norm", "year"]
df = pd.read_csv("data/breton_devri.csv", sep=",", names=col_names)

