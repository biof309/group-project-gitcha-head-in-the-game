#create instance of standard scaler
scaler=StandardScaler()

#
feature_array=characteristics.values
feature_array=feature_array.astype(float)
type(feature_array[0,0]) #check that it's a
np.mean(feature_array[:,0])
np.std(feature_array[:,0])


#scale
scaled_features=scaler.fit_transform(feature_array)
#check scaling
np.mean(scaled_features[:,0])
np.std(scaled_features[:,0])




