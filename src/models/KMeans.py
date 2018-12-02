kmeans=KMeans(n_clusters=5)

kmeans.fit(scaled_features)

clusters=kmeans.predict(scaled_features)

breedlist=list(breeds.values.T.flatten())

clustered_breeds=pd.DataFrame({'clusters':clusters, 'breeds':breedlist})

clustered_breeds=clustered_breeds.sort_values(by='clusters')