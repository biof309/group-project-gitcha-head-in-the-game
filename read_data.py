import pandas as pd

dogs = pd.read_csv('https://query.data.world/s/wb2m35hoycwvieh3455mrac6l5ewjs', encoding="ISO-8859-1")
dogs.head()



#Removing "na" and "not found"
dogs[dogs=='na']=np.nan
dogs[dogs=='not found']=np.nan
print(dogs.isnull().sum())
dogs.shape
dogs= dogs.dropna()
dogs.shape

#Take out column "Breed"
characteristics = dogs.iloc[:, 1:]

characteristics_array = characteristics.values
type(characteristics_array)

characteristics_array = characteristics_array.astype(float)
type(characteristics_array[0,0])

print(characteristics_array)

#separate into height array and weight array
columns_height = characteristics_array[:,0:2]
columns_weight = characteristics_array[:,2:4]

#Find average low height and average high height
average_height_wholecolumn = np.mean(columns_height, axis = 0)

#Find average height and weight for each breed
average_height = np.mean(columns_height, axis = 1)
print(average_height)

average_weight = np.mean(columns_weight, axis = 1)
print(average_weight)

#Convert average height and average weight rows into columns
average_height_column0 = np.array([average_height])
average_height_column = average_height_column0.T
print(average_height_column)

average_weight_column0 = np.array([average_weight])
average_weight_column = average_weight_column0.T
print(average_height_column)

#Add average height and average weight as new columns to characteristics
Characteristics_with_average_height = np.append(columns_height, average_height_column, axis=1)

Characteristics_with_average_weight = np.append(columns_weight, average_weight_column, axis=1)

Characteristics_Total = np.append(Characteristics_with_average_height,Characteristics_with_average_weight, axis=1)









