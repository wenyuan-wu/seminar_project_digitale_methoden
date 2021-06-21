import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results_tiny.csv')
# print(df)
x_labels = ["Norma", "cSMTiser", "Marian", "Neural Transducer"]
# Plot the figure.
plt.figure(figsize=(16, 12))
ax = df.plot(kind='bar')
ax.set_title('Results on tiny dataset (150)')
ax.set_ylabel('Scores')
ax.set_xlabel('Methods')
ax.set_xticklabels(x_labels, rotation="horizontal")
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=True) # labels along the bottom edge are off

# plt.show()
plt.savefig("results_tiny.png")

df = pd.read_csv('results_small.csv')
# print(df)
x_labels = ["Norma", "cSMTiser", "Marian", "Neural Transducer"]
# Plot the figure.
plt.figure(figsize=(16, 12))
ax = df.plot(kind='bar')
ax.set_title('Results on small dataset (625)')
ax.set_ylabel('Scores')
ax.set_xlabel('Methods')
ax.set_xticklabels(x_labels, rotation="horizontal")
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=True) # labels along the bottom edge are off

# plt.show()
plt.savefig("results_small.png")

df = pd.read_csv('tendency_accuracy.csv')
# print(df)
x_labels = ["150", "625"]
# Plot the figure.
plt.figure(figsize=(16, 12))
ax = df.plot(kind='line')
ax.set_title('Tendency of word accuracy')
ax.set_ylabel('Scores')
ax.set_xlabel('dataset size')
ax.set_xticks([0, 1])
ax.set_xticklabels(x_labels, rotation="horizontal")
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=True) # labels along the bottom edge are off

# plt.show()
plt.savefig("tendency_accuracy.png")

df = pd.read_csv('tendency_cer.csv')
# print(df)
x_labels = ["150", "625"]
# Plot the figure.
plt.figure(figsize=(16, 12))
ax = df.plot(kind='line')
ax.set_title('Tendency of average CER')
ax.set_ylabel('Scores')
ax.set_xlabel('dataset size')
ax.set_xticks([0, 1])
ax.set_xticklabels(x_labels, rotation="horizontal")
# plt.tick_params(
#     axis='x',          # changes apply to the x-axis
#     which='both',      # both major and minor ticks are affected
#     bottom=False,      # ticks along the bottom edge are off
#     top=False,         # ticks along the top edge are off
#     labelbottom=True) # labels along the bottom edge are off

# plt.show()
plt.savefig("tendency_cer.png")
