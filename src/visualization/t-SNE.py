from matplotlib import cm
from sklearn.manifold import TSNE
#create instance of t-SNE
tsne=TSNE(learning_rate=100)
#fit t-SNE featres
tsne_features=tsne.fit_transform(scaled_features)

#make x and y for graph
x=tsne_features[:,0]
y=tsne_features[:,1]

breedlist=list(breeds.values.T.flatten())
unique_clusters=list(set(clusters))
cmap=cm.get_cmap("viridis",5)

plt.scatter(x,y, alpha=0.5, c=clusters, label=unique_clusters, cmap=cmap, vmin=-0.5, vmax=4.4)
c=plt.colorbar(ticks=unique_clusters)
c.set_label('KMeans clusters')
plt.title('T-SNE Plot of Dog Breeds')
for x,y,breed in zip(x,y,breedlist):
    plt.annotate(breed, (x,y), fontsize=4, alpha=0.5)

plt.savefig('src/visualization/tSNE')



