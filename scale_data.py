scaler=StandardScaler()

scaled=scaler.fit_transform(characteristics)
np.mean(dogs.loc[:,"height_low_inches"])

x=dogs.loc[:,"height_low_inches"]

print(x.apply(np.mean))

print(x.mean)

x=dogs['height_high_inches']

dogs.loc[:,'height_high_inches'].mean()

dogs['height_high_inches'].astype(float)

type(dogs['height_high_inches'])

x_scaled=scale(x)

array=characteristics.values
type(array)


print(array.mean)