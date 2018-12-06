import seaborn as sns
sns.pairplot(Characteristics_Total_df)
fig=plt.gcf()
fig.suptitle('Dog Breed Characteristics', size=20)
fig.set_size_inches(11,10)
plt.savefig('src/visualization/pairplot.png')