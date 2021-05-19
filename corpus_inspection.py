import pandas as pd
import matplotlib.pyplot as plt

col_names = ["hist", "norm", "year"]
df = pd.read_csv("data/breton_devri.csv", sep=",", names=col_names)

print(len(df))

x_labels = ["avant 1100",
            "1100 - 1449",
            "1450 - 1559",
            "1600 - 1650",
            "1651 - 1799",
            "1800 - 1899",
            "1900 - 1999",
            "depuis 2000"
            ]

frequencies = []

df_1 = df[df["year"] < 1100]
frequencies.append(len(df_1))

df_2 = df[df["year"].between(1100, 1450)]
frequencies.append(len(df_2))

df_3 = df[df["year"].between(1450, 1600)]
frequencies.append(len(df_3))

df_4 = df[df["year"].between(1600, 1651)]
frequencies.append(len(df_4))

df_5 = df[df["year"].between(1651, 1800)]
frequencies.append(len(df_5))

df_6 = df[df["year"].between(1800, 1900)]
frequencies.append(len(df_6))

df_7 = df[df["year"].between(1900, 2000)]
frequencies.append(len(df_7))

df_8 = df[df["year"] > 2000]
frequencies.append(len(df_8))

freq_series = pd.Series(frequencies)

# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Period Distribution')
ax.set_ylabel('Amount')
ax.set_xticklabels(x_labels, rotation="horizontal")

rects = ax.patches

for rect, val in zip(rects, frequencies):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, val,
            ha='center', va='bottom')

plt.savefig("period_distribution.png")
