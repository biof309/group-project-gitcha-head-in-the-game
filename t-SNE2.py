tsne2=TSNE(learning_rate=100)

tsne_features2=tsne2.fit_transform(feature_array)


x2=tsne_features2[:,0]
y2=tsne_features2[:,1]

plt.scatter(x2,y2, alpha=0.5)
for x2,y2,breed in zip(x2,y2,breedlist):
    plt.annotate(breed, (x2,y2), fontsize=5)
plt.show()