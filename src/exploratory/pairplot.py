import seaborn as sns
sns.pairplot(Characteristics_Total_df)
plt.suptitle('Dog Breed Characteristics', size=30)

plt.savefig(src/visualization/pairplot.png)