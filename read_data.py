import pandas as pd

df = pd.read_csv('https://query.data.world/s/wb2m35hoycwvieh3455mrac6l5ewjs', encoding="ISO-8859-1")
df.head()
characteristics = df.iloc[:, 1:]
breeds = df.iloc[:, :1]
characteristics.head()
breeds.head()
