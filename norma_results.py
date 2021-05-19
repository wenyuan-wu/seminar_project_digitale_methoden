import pandas as pd
from sklearn.metrics import precision_score
from devri_web import get_char_bleu
import matplotlib.pyplot as plt

col_names_gs = ["hist", "norm"]
df_gs = pd.read_csv("data/period_7_test.csv", sep="\t", names=col_names_gs)
# print(df_gs)
y_true = df_gs["norm"]

col_names_pred = ["norm", "score"]
df_pred = pd.read_csv("norma_files/period_7_predictions.csv", sep="\t", names=col_names_pred)
y_pred = df_pred["norm"]
# print(df_pred)

score = precision_score(y_true, y_pred, average="micro")

print(score)

bleu_scores = []

for true, pred in zip(y_true, y_pred):
    bleu_scores.append(get_char_bleu(pred, true))

bleu_avg = sum(bleu_scores) / len(bleu_scores)


freq_series = pd.Series(bleu_scores)

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
