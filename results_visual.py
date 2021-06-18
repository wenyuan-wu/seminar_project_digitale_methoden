import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')
print(df)

# TODO
# Plot the figure.
plt.figure(figsize=(12, 8))
ax = freq_series.plot(kind='bar')
ax.set_title('Norma BLEU score on test set')
ax.set_ylabel('character BLEU')
ax.set_xlabel('tokens')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

plt.savefig("norma_bleu.png")

print(bleu_avg)