from sklearn.cluster import KMeans
#create instance of KMeans clusters
kmeans=KMeans(n_clusters=5)

#fit to data
kmeans.fit(scaled_features)
#predict clusters
clusters=kmeans.predict(scaled_features)

#which breed does each cluster belong to
breedlist=list(breeds.values.T.flatten())
clustered_breeds=pd.DataFrame({'clusters':clusters, 'breeds':breedlist})
clustered_breeds=clustered_breeds.sort_values(by='clusters')
clustered_breeds.to_csv("clustered_breeds.txt")
