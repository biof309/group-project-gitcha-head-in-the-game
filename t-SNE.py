tsne=TSNE(learning_rate=200)

tsne_features=tsne.fit_transform(scaled_features)

x=tsne_features[:,0]
y=tsne_features[:,1]

plt.scatter(x,y, alpha=0.5)
for x,y,breed in zip()
plt.show()



breedlist=list(breeds.values.flatten())
print(breedlist)
print(*breedlist.flat)
print(breedlist.T)