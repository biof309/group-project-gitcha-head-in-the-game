import pandas as pd

dogs = pd.read_csv('https://query.data.world/s/wb2m35hoycwvieh3455mrac6l5ewjs', encoding="ISO-8859-1")
dogs.head()




dogs[dogs=='na']=np.nan
dogs[dogs=='not found']=np.nan
print(dogs.isnull().sum())
dogs.shape
dogs= dogs.dropna()
dogs.shape