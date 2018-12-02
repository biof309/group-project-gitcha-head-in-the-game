tsne=TSNE(learning_rate=100)

tsne_features=tsne.fit_transform(scaled_features)

x=tsne_features[:,0]
y=tsne_features[:,1]

breedlist=list(breeds.values.T.flatten())



plt.scatter(x,y, alpha=0.5, c=clusters)



for x,y,breed in zip(x,y,breedlist):
    plt.annotate(breed, (x,y), fontsize=5)
plt.show()




