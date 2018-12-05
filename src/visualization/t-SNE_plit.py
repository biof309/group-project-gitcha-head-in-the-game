a=pd.DataFrame({'clusters':clusters, 'breeds':breedlist, 'tsne0':tsne_features[:,0], 'tsne1':tsne_features[:,1]})
cluster0=a[a['clusters']==0]
cluster1=a[a['clusters']==1]
cluster2=a[a['clusters']==2]
cluster3=a[a['clusters']==3]
cluster4=a[a['clusters']==4]

plt.scatter(x=cluster0['tsne0'],y=cluster0['tsne1'], alpha=0.5, c='red')
plt.title('KMeans Cluster 0')
zip0=zip(list(cluster0.tsne0), list(cluster0.tsne1), list(cluster0.breeds))
for x,y,breed in zip0:
    plt.annotate(breed, (x,y), fontsize=6, alpha=0.5)
plt.savefig('src/visualization/cluster0.png')
plt.close()


plt.scatter(x=cluster1['tsne0'],y=cluster1['tsne1'], alpha=0.5, c='blue')
plt.title('KMeans Cluster 1')
zip1=zip(list(cluster1.tsne0), list(cluster1.tsne1), list(cluster1.breeds))
for x,y,breed in zip1:
    plt.annotate(breed, (x,y), fontsize=6, alpha=0.5)
plt.savefig('src/visualization/cluster1.png')
plt.close()

plt.scatter(x=cluster2['tsne0'],y=cluster2['tsne1'], alpha=0.5, c='purple')
plt.title('KMeans Cluster 2')
zip2=zip(list(cluster2.tsne0), list(cluster2.tsne1), list(cluster2.breeds))
for x,y,breed in zip2:
    plt.annotate(breed, (x,y), fontsize=6, alpha=0.5)
plt.savefig('src/visualization/cluster2.png')
plt.close()

plt.scatter(x=cluster3['tsne0'],y=cluster3['tsne1'], alpha=0.5, c='yellow')
plt.title('KMeans Cluster 3')
zip3=zip(list(cluster3.tsne0), list(cluster3.tsne1), list(cluster3.breeds))
for x,y,breed in zip3:
    plt.annotate(breed, (x,y), fontsize=6, alpha=0.5)
plt.savefig('src/visualization/cluster3.png')
plt.close()

plt.scatter(x=cluster4['tsne0'],y=cluster4['tsne1'], alpha=0.5, c='purple')
plt.title('KMeans Cluster 4')
zip4=zip(list(cluster4.tsne0), list(cluster4.tsne1), list(cluster4.breeds))
for x,y,breed in zip4:
    plt.annotate(breed, (x,y), fontsize=6, alpha=0.5)
plt.savefig('src/visualization/cluster4.png')
plt.close()