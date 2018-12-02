kmeans=KMeans(n_clusters=5)

kmeans.fit(scaled_features)

clusters=kmeans.predict(scaled_features)


