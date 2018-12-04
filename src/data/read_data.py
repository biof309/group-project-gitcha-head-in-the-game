import pandas as pd
import numpy as np

dogs = pd.read_csv('https://query.data.world/s/wb2m35hoycwvieh3455mrac6l5ewjs', encoding="ISO-8859-1")
dogs.head()


#Removing "na" and "not found"
dogs[dogs=='na']=np.nan
dogs[dogs=='not found']=np.nan
print(dogs.isnull().sum())
dogs.shape
dogs= dogs.dropna()
dogs.shape

print(dogs)

import matplotlib.pyplot as plt
from pandas.tools.plotting import table

import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table
import numpy as np


df.index = [item.strftime('%Y-%m-%d') for item in df.index] # Format date

fig, ax = plt.subplots(figsize=(12, 2)) # set size frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
tabla = table(ax, Dogs, loc='upper right', colWidths=[0.17]*len(df.columns))  # where df is your data frame
tabla.auto_set_font_size(False) # Activate set fontsize manually
tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
tabla.scale(1.2, 1.2) # change size table
plt.savefig('table.png', transparent=True)



